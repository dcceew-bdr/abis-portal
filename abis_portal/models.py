from enum import Enum

from pydantic import BaseModel


class SupportedFormats(Enum):
    TURTLE_FORMAT = "text/turtle"
    JSON_FORMAT = "application/json"
    JSON_LD_FORMAT = "application/ld+json"
    EXCEL_FORMAT = "application/vnd.ms-excel"


class ValidateIn(BaseModel):
    data: str
    format: SupportedFormats
    shacl_shapes: str

