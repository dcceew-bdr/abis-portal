import json

import httpx
from jsonschema import validate
from jsonschema.exceptions import ValidationError  # imported here for downstream to use

from geochem_portal.fetch import fetch
from geochem_portal.settings import settings


async def json_to_rdf(data: str) -> str:
    async with httpx.AsyncClient() as client:
        schema = await fetch(
            client,
            f"{settings.geochem_spec_base_cdn}{settings.geochem_spec_version}/profiles/gsq/schema.json",
            to_json=True,
        )
        context = await fetch(
            client,
            f"{settings.geochem_spec_base_cdn}{settings.geochem_spec_version}/profiles/gsq/context.json",
            to_json=True,
        )

    json_data = json.loads(data)
    validate(instance=json_data, schema=schema)

    json_ld = {**context, **{"@graph": data}}

    return json.dumps(json_ld)
