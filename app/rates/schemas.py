from typing import Optional

from pydantic import BaseModel


class SRate(BaseModel):
    rate_mark: str
    comment: Optional[str] = None
    user: int
    product: int

    class Config:
        orm_mode = True


class RateUpdate(BaseModel):
    rate_mark: str
    comment: Optional[str] = None
