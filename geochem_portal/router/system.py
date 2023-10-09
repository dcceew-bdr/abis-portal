from fastapi import APIRouter
from pydantic import BaseModel

from geochem_portal.settings import settings

router = APIRouter()


class VersionDetail(BaseModel):
    version: str


@router.get("/version")
def version_route():
    """VocExcel application version."""
    return VersionDetail(version=settings.geochem_portal_version)
