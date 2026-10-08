from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd

from app.database import get_db
from app.models import Sale
from app.schemas import AnalyticsSummary

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/summary", response_model=AnalyticsSummary)
def get_analytics_summary(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()

    # Проверка: если в базе нет продаж, отдаем понятную ошибку 404
    if not sales:
        raise HTTPException(
            status_code=404, detail="В базе данных пока нет записей о продажах"
        )

    data = [
        {
            "id": s.id,
            "product_name": s.product_name,
            "category": s.category,
            "amount": s.amount,
            "quantity": s.quantity,
            "sale_date": s.sale_date,
        }
        for s in sales
    ]
    df = pd.DataFrame(data)

    df["total_amount"] = df["amount"] * df["quantity"]

    total_revenue = float(df["total_amount"].sum())
    total_sales_count = int(len(df))
    average_check = float(df["total_amount"].mean())

    category_revenue = df.groupby("category")["total_amount"].sum()
    top_category = str(category_revenue.idxmax())

    return AnalyticsSummary(
        total_revenue=round(total_revenue, 2),
        total_sales_count=total_sales_count,
        average_check=round(average_check, 2),
        top_category=top_category,
    )