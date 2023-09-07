import uvicorn


if __name__ == "__main__":
    uvicorn.run("geochem_portal.app:create_app", reload=True)
