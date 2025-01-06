from fastapi import FastAPI

app = FastAPI(
    title="EIMS",
    description="E-commerce Inventory Management System API",
    version="0.1.0"
)


@app.get("/")
def index():
    return {"message": "Welcome to the EIMS!"}
