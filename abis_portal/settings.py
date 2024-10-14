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
    abis_spec_version: str = "8508db14ff87276349f2658cf536efef5c1cf626"
    abis_spec_base_cdn: str = (
        "https://cdn.jsdelivr.net/gh/Kurrawong/gsq-abis-spec@"
    )


settings = Settings(_env_file=".env")
