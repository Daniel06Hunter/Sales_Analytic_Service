from fastapi import APIRouter, Depends
from app.schemas import SaleCreate, SaleResponse
from sqlalchemy.orm import Session
from app.models import Sale
from app.database import get_db 

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("/", response_model=SaleResponse)
async def post_sale(sale:SaleCreate, db:Session = Depends(get_db)): 
    db_sale = Sale(**sale.model_dump())  # Создаем экземпляр ORM-модели
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


@router.get("/", response_model = list[SaleResponse])
async def get_sales(db:Session = Depends(get_db)): 
    db.query(Sale).all()
    return db


    