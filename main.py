import os
import asyncio
from fastapi import FastAPI, status, Body
from decouple import config
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from irodori_api.models import GiftBase
from datetime import datetime
from starlette.responses import JSONResponse

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

DB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://kenakai:aNNgX5QhZh7AICPH@cluster0.giyxphh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = config("DB_NAME", cast=str)

app = FastAPI(middleware=middleware)


async def get_database():
    client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)
    return client[DB_NAME]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/api/gifts", response_description="Add new Gift")
async def create_gift(gift: GiftBase = Body(...)):
    db = await get_database()

    portfolio = jsonable_encoder(gift)
    portfolio["created_at"] = datetime.now().isoformat()
    new_portfolio = await db["gifts"].insert_one(portfolio)
    created_portfolio = await db["gifts"].find_one(
        {"_id": new_portfolio.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_portfolio)
