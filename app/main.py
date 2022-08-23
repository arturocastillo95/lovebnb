from fastapi import FastAPI
from core.config import settings
# import uvicorn

def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)
    return app

app = start_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/create-listing")
async def create_listing():
    return {"message": "Create Listing"}

@app.get("/listings")
async def listings():
    return {"message": "Listings"}

# if __name__ == "__main__":
#     uvicorn.run(app)

 