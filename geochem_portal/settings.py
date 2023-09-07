from importlib import metadata
from os import environ

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    ...


def get_version() -> str:
    try:
        version = metadata.version("geochem_portal")
    except metadata.PackageNotFoundError:
        version = "0.0.0-dev.0"

    return version


class Settings:
    GEOCHEM_PORTAL_VERSION = get_version()
    GEOCHEM_PORTAL_STATIC_DIR = environ.get(
        "GEOCHEM_PORTAL_STATIC_DIR", "geochem_portal/static"
    )
