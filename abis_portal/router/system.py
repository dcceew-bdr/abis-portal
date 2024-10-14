from fastapi import APIRouter
from pydantic import BaseModel

from abis_portal.settings import settings

router = APIRouter()


class VersionDetail(BaseModel):
    version: str


@router.get("/version")
def version_route():
    """VocExcel application version."""
    return VersionDetail(version=settings.abis_portal_version)
