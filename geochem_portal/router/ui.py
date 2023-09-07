from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from geochem_portal.settings import Settings

router = APIRouter()


@router.get("/{path:path}", include_in_schema=False)
def all_path_route(path):
    """Catch-all route for SPA."""
    index_html_path = Path(f"{Settings.GEOCHEM_PORTAL_STATIC_DIR}/index.html")

    path = (
        Path(f"{Settings.GEOCHEM_PORTAL_STATIC_DIR}/{path}")
        if path != ""
        else index_html_path
    )

    if path.is_file():
        return FileResponse(path)

    return FileResponse(index_html_path)
