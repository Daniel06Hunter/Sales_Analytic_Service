from pydantic import BaseModel 
from datetime import datetime


class SaleBase(BaseModel): 
    product_name:str
    category: str 
    amount: float
    quantity: int 
    
class SaleCreate(SaleBase): 
    pass

class SaleResponse(SaleBase): 
    id:int
    sale_date:datetime
    class Config: 
        from_attributes = True # Позволяет Pydantic читать данные прямо из ORM-моделей SQLAlchemy
        
        
class AnalyticsSummary(BaseModel): 
    total_revenue:float       
    total_sales_count: int 
    averaeg_check : float 
    top_category:  str 
    
      
