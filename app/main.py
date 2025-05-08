from fastapi import FastAPI
from app.api.endpoints import clinics, upa, ubs

app = FastAPI(title="Api Saude")

app.include_router(clinics.router, prefix="/clinics")
app.include_router(upa.router, prefix="/clinics/upa")
app.include_router(ubs.router, prefix="/clinics/ubs")

@app.get("/")
def read_root():
    return {"Hello": "World"}