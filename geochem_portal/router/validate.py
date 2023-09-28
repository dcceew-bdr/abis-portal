from pathlib import Path

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from rdflib import Graph

from geochem_portal.validate import validate, ParseError

router = APIRouter()


class ValidateIn(BaseModel):
    data: str
    shacl_shapes: str


def process_and_load_background_data(data: str) -> str:
    """Process data and load background data for geochemistry validation.

    The incoming data is processed with a SPARQL query before
    loading additional background data. This function is intended to be
    called before SHACL validation is performed.

    :param data: Incoming data in RDF Turtle format.
    :return: RDF Turtle data after processing and the addition of background data added.
    """
    graph = Graph()
    graph.parse(data=data)

    with open(
        "geochem_portal/data_files/oc-to-o.sparql", "r", encoding="utf-8"
    ) as file:
        graph.update(file.read())

    files = Path("geochem_portal/data_files").glob("**/*.ttl")
    for file in files:
        graph.parse(file)

    return graph.serialize(format="turtle")


@router.post("/validate")
def validate_route(validate_in_data: ValidateIn):
    try:
        data = process_and_load_background_data(validate_in_data.data)
        report = validate(data, validate_in_data.shacl_shapes)
    except ParseError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err))

    return report
