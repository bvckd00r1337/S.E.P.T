from sqlalchemy import Column, Integer, String, Date, Numeric, BigInteger, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stocks(Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String(10), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    volume = Column(BigInteger)
    
    __table_args__ = (UniqueConstraint('symbol', 'date', name='_symbol_date_uc'),)