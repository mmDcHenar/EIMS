from fastapi import FastAPI
from app.routers import api_router


app = FastAPI(
    title="EIMS",
    description="E-commerce Inventory Management System API",
    version="0.1.0"
)

app.include_router(api_router)


@app.get("/")
def index():
    return {"message": "Welcome to the EIMS!"}
