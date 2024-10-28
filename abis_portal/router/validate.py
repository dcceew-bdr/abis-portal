from fastapi import APIRouter, HTTPException, status
from rdflib import Graph
from starlette.requests import Request

from abis_portal.models import SupportedFormats, ValidateIn
from abis_portal.queries import get_oc_to_o_query
from abis_portal.settings import settings
from abis_portal.validate import validate, ParseError
from abis_portal.validate_json import (
    json_to_rdf,
    ValidationError as JSONSchemaValidationError,
)

router = APIRouter()


async def process_and_load_background_data(data: str, media_type: str) -> str:
    """Process data and load background data for abisistry validation.

    The incoming data is processed with a SPARQL query before
    loading additional background data. This function is intended to be
    called before SHACL validation is performed.

    :param data: Incoming data in RDF Turtle format.
    :return: RDF Turtle data after processing and the addition of background data added.
    """
    graph = Graph()
    graph.parse(data=data, format=media_type)

    query = get_oc_to_o_query()
    graph.update(query)

    commit = settings.abis_spec_version
    base_cdn_url = settings.abis_spec_base_cdn

    # files = [
    #     "profiles/gsq/vocabs/analytical-methods-for-abisistry.ttl",
    #     "profiles/gsq/vocabs/geou.ttl",
    #     "profiles/gsq/vocabs/idn-role-codes.ttl",
    #     "profiles/gsq/vocabs/observable-properties.ttl",
    #     "profiles/gsq/vocabs/sample-types.ttl",
    # ]
    #
    # print("Fetching external data sources.")
    # start_time = time.time()
    # async with httpx.AsyncClient() as client:
    #     urls = [f"{base_cdn_url}{commit}/{file}" for file in files]
    #     tasks = [fetch(client, url) for url in urls]
    #     results = await asyncio.gather(*tasks)
    #
    #     for result in results:
    #         graph.parse(data=result)
    #
    # print(f"Done fetching. Time taken: {time.time() - start_time:.2f} seconds.")
    return graph.serialize(format="turtle")


@router.post("/validate")
async def validate_route(
        validate_data: ValidateIn,
        request: Request
):
    try:
        match validate_data.format:
            case SupportedFormats.EXCEL_FORMAT:
                raise NotImplementedError("Excel format not supported yet.")
            case SupportedFormats.JSON_FORMAT:
                data = await json_to_rdf(validate_data.data)
                media_type = SupportedFormats.JSON_LD_FORMAT
            case media_type:
                data = await process_and_load_background_data(
                    validate_data.data, media_type.value
                )

        shacl_graph = request.app.state.shacl_graphs[validate_data.shacl_shapes]

        report = validate(
            data=data,
            shacl_shapes=validate_data.shacl_shapes,
            format=media_type.value,
            shacl_graph=shacl_graph
        )

        return report

    except ParseError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err)) from err
    except JSONSchemaValidationError as err:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            f"JSON Schema validation failed. {err}"
        ) from err
