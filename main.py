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

DB_URL = "mongodb+srv://kenakai:aNNgX5QhZh7AICPH@cluster0.giyxphh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = config("DB_NAME", cast=str)
origins = ["*"]
app = FastAPI(middleware=middleware)

# グローバル変数としてクライアントとデータベースを定義
mongodb_client = None
mongodb = None


@app.on_event("startup")
async def startup_db_client():
    global mongodb_client, mongodb
    mongodb_client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)
    mongodb = mongodb_client[DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    if mongodb_client:
        mongodb_client.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/api/gifts", response_description="Add new Gift")
async def create_gift(gift: GiftBase = Body(...)):
    global mongodb
    if mongodb is None:
        await startup_db_client()

    portfolio = jsonable_encoder(gift)
    portfolio["created_at"] = datetime.now().isoformat()
    new_portfolio = await mongodb["gifts"].insert_one(portfolio)
    created_portfolio = await mongodb["gifts"].find_one(
        {"_id": new_portfolio.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_portfolio)
