import logging
from fastapi import APIRouter, HTTPException
import json
import os
from typing import List
from app.models.portfolio import PortfolioPosition

portfolio_router = APIRouter()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@portfolio_router.get("/sipp", response_model=List[PortfolioPosition])
async def get_portfolio_positions() -> List[PortfolioPosition]:
    file_path = "data/portfolio.json"
    
    if not os.path.exists(file_path):
        logger.error(f"Portfolio data file not found at {file_path}")
        raise HTTPException(status_code=404, detail="Portfolio data not found")
    
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return [PortfolioPosition(**position) for position in data]
    except Exception as e:
        logger.error(f"Error invoking chain: {e}")
        raise HTTPException(status_code=500, detail=f"Unable to retrieve portfolio account")
