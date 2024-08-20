import enum

from sqlalchemy import Column, String, DateTime, BigInteger, Integer

from app.settings.db import Base


class Rate(Base):
    __tablename__ = 'rates'

    deleted_at = Column(DateTime, nullable=True)
    rate_mark = Column(Integer)
    comment = Column(String, nullable=True)
    user = Column(BigInteger, nullable=False)
    product = Column(BigInteger, nullable=False)
