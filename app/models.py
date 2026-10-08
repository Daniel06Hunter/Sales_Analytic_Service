from datetime import datetime 
from sqlalchemy import Column, Integer, DateTime, Float, String
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

class Sale(Base): 
    __tablename__="sales"
    
    id = Column(Integer, primary_key = True, index=True)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    quantity = Column(Integer, nullable = False)
    sale_date = Column(DateTime, default = datetime.utcnow, nullable = False)
    
    