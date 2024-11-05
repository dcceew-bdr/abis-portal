from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyshacl.monkey import rdflib_bool_patch, rdflib_bool_unpatch
from pyshacl.rdfutil import load_from_source
from rdflib import Graph

from abis_portal import router
import logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.shacl_graphs = {}
    known_validators = {
        "BDR Validator": "bdr-profile.ttl",
        "ABIS Validator": "abis.ttl",
        "TERN Ontology Validator": "tern.ttl",
    }

    for validator_name, file_name in known_validators.items():
        shacl_graph = Graph()
        with open(f"abis_portal/validators/{file_name}") as f:
            shacl_graph.parse(f, format="text/turtle")
        rdflib_bool_patch()
        loaded_sg = load_from_source(
            shacl_graph, rdf_format="text/turtle", multigraph=True, do_owl_imports=True
        )
        rdflib_bool_unpatch()
        app.state.shacl_graphs[validator_name] = loaded_sg

    yield
    # Shutdown
    app.state.shacl_graphs.clear()


def register_routers(app: FastAPI) -> None:
    app.include_router(router.system.router, prefix="/api/v1/system", tags=["System"])
    app.include_router(router.validate.router, prefix="/api/v1", tags=["Validation"])
    app.include_router(router.ui.router)


def register_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title="BDR ABIS Portal API",
        description="BDR ABIS Data Portal API provides functions to validate and submit abisistry data.",
        lifespan=lifespan
    )

    register_routers(app)
    register_middlewares(app)

    return app
