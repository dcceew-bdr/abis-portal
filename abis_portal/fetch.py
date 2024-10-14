import time

import httpx


async def fetch(
    client: httpx.AsyncClient, url: str, to_json: bool = False
) -> str | dict:
    start_time = time.time()
    response = await client.get(url)
    print(f"Done fetching. Time taken: {time.time() - start_time:.2f} seconds.")

    if response.status_code != 200:
        raise httpx.HTTPError(
            f"Sending request received unexpected status code {response.status_code}. URL: {url}. {response.text}"
        )

    return response.text if not to_json else response.json()
