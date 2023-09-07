from fastapi import APIRouter
from pydantic import BaseModel

from geochem_portal.settings import Settings

router = APIRouter()


class VersionDetail(BaseModel):
    version: str


@router.get("/version")
def version_route():
    """VocExcel application version."""
    return VersionDetail(version=Settings.GEOCHEM_PORTAL_VERSION)
