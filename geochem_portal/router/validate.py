import time
import asyncio

import httpx
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from rdflib import Graph

from geochem_portal.validate import validate, ParseError
from geochem_portal.queries import get_oc_to_o_query

router = APIRouter()


class ValidateIn(BaseModel):
    data: str
    shacl_shapes: str


async def fetch(client: httpx.AsyncClient, url: str) -> str:
    response = await client.get(url)
    response.raise_for_status()
    return response.text


async def process_and_load_background_data(data: str) -> str:
    """Process data and load background data for geochemistry validation.

    The incoming data is processed with a SPARQL query before
    loading additional background data. This function is intended to be
    called before SHACL validation is performed.

    :param data: Incoming data in RDF Turtle format.
    :return: RDF Turtle data after processing and the addition of background data added.
    """
    graph = Graph()
    graph.parse(data=data)

    query = get_oc_to_o_query()
    graph.update(query)

    # TODO: hardcoded commit
    commit = "ab38732e128669989f14aba3b52eb88a5f01d1d8"
    base_cdn_url = "https://cdn.jsdelivr.net/gh/Kurrawong/gsq-geochem-spec@"

    files = [
        "/vocabs/analytical-methods-for-geochemistry.ttl",
        "/vocabs/geou.ttl",
        "/vocabs/idn-role-codes.ttl",
        "/vocabs/observable-properties.ttl",
        "/vocabs/sample-types.ttl",
    ]

    print("Fetching external data sources.")
    starttime = time.time()
    async with httpx.AsyncClient() as client:
        urls = [f"{base_cdn_url}{commit}{file}" for file in files]
        tasks = [fetch(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for result in results:
            graph.parse(data=result)

    print(f"Done fetching. Time taken: {time.time() - starttime:.2f} seconds.")
    return graph.serialize(format="turtle")


@router.post("/validate")
async def validate_route(validate_in_data: ValidateIn):
    try:
        data = await process_and_load_background_data(validate_in_data.data)
        report = validate(data, validate_in_data.shacl_shapes)
    except ParseError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err))

    return report
