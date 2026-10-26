from pydantic import BaseModel
"""
Model for representing a position in the portfolio.

"""
class PortfolioPosition(BaseModel):
    symbol: str
    name: str
    quantity: int
    price: float
    currency: str
    book_cost: float
    average_price: float
