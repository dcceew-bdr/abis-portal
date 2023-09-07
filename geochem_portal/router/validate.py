from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from geochem_portal.validate import validate, ParseError

router = APIRouter()


class ValidateIn(BaseModel):
    data: str
    shacl_shapes: str


@router.post("/validate")
def validate_route(validate_in_data: ValidateIn):
    try:
        report = validate(validate_in_data.data, validate_in_data.shacl_shapes)
    except ParseError as err:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(err))

    return report
