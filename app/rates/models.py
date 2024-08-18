import enum

from sqlalchemy import Column, String, DateTime, Enum, BigInteger

from app.settings.db import Base


class MarkEnum(enum.Enum):
    GREAT = 5
    GOOD = 4
    OKEY = 3
    BAD = 2
    AWFUL = 1


class Rate(Base):
    __tablename__ = 'rates'

    deleted_at = Column(DateTime, nullable=True)
    rate_mark = Column(Enum(MarkEnum))
    comment = Column(String, nullable=True)
    user = Column(BigInteger, nullable=False)
    product = Column(BigInteger, nullable=False)