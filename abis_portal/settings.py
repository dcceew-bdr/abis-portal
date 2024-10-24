from importlib import metadata

from pydantic_settings import BaseSettings


def get_version() -> str:
    try:
        version = metadata.version("abis_portal")
    except metadata.PackageNotFoundError:
        version = "0.0.0-dev.0"

    return version


class Settings(BaseSettings):
    abis_portal_version: str = get_version()
    abis_portal_static_dir: str = "abis_portal/static"
    abis_spec_version: str = "71e71bdd8c1e52588dd2761d9ebfae7f4171d48a"
    abis_spec_base_cdn: str = (
        "https://cdn.jsdelivr.net/gh/AusBIGG/abis@"
    )


settings = Settings(_env_file=".env")
