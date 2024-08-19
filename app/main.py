from fastapi import FastAPI
from app.rates.router import router as rates_router
app = FastAPI()

app.include_router(rates_router, prefix='/api/v1')
