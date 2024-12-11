from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from app.routers import data_processing
from app.core.config import settings
from app.core.dependencies import get_cache_key

app = FastAPI(
    title="API de Processamento de Dados",
    description="API RESTful para processamento e análise de grandes volumes de dados",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

app.include_router(data_processing.router, prefix="/api/v1")

@app.get("/")
@cache(expire=60, key_builder=get_cache_key)
async def root():
    return {"message": "Bem-vindo à API de Processamento de Dados"} 