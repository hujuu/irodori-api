from fastapi import Depends, FastAPI, Response, Request, status, Body
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


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL, tls=True, tlsAllowInvalidCertificates=True)
    app.mongodb = app.mongodb_client[DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/api/gifts", response_description="Add new Gift")
async def create_gift(
        request: Request,
        portfolio: GiftBase = Body(...)):
    portfolio = jsonable_encoder(portfolio)
    portfolio["created_at"] = datetime.now().isoformat()

    new_portfolio = await request.app.mongodb["gifts"].insert_one(portfolio)
    created_portfolio = await request.app.mongodb["gifts"].find_one(
        {"_id": new_portfolio.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_portfolio)
