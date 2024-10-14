import azure.functions as func

from abis_portal.app import create_app

fastapi_app = create_app()

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
