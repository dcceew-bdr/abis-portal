import uvicorn


if __name__ == "__main__":
    uvicorn.run("abis_portal.app:create_app", reload=True, port=7071)
