from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from geochem_portal.settings import settings

router = APIRouter()


@router.get("/{path:path}", include_in_schema=False)
def all_path_route(path):
    """Catch-all route for SPA."""
    index_html_path = Path(f"{settings.geochem_portal_static_dir}/index.html")

    path = (
        Path(f"{settings.geochem_portal_static_dir}/{path}")
        if path != ""
        else index_html_path
    )

    if path.is_file():
        return FileResponse(path)

    return FileResponse(index_html_path)
