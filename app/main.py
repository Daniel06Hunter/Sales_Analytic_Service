from fastapi import FastAPI
from app.api.analytics import router as analytics_router
from app.api.endpoints import router as sales_router
from app.database import engine
from app.models import Base

# Создаем таблицы в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sales Analytics Service")

# Подключаем роутер с эндпоинтами /sales/
app.include_router(sales_router)
app.include_router(analytics_router)

@app.get("/healthcheck")
def get_healthcheck():
    return {"status": "ok"}