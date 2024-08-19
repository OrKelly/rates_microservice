from typing import Any

from app.rates.dao import RatesDAO
from app.rates.exceptions import RateNotFound


async def valid_rate_id(rate_id: int) -> dict[str, Any]:
    existing_rate = await RatesDAO.find_one_or_none(id=rate_id)
    if not existing_rate:
        raise RateNotFound
    return existing_rate
