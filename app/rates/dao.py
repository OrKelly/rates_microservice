from sqlalchemy import select, func, desc

from app.base_dao.dao import BaseDAO
from app.rates.models import Rate
from app.settings.db import async_session_maker


class RatesDAO(BaseDAO):
    model = Rate

    @classmethod
    async def get_product_rate_stat(cls, product_id: int):
        async with async_session_maker() as session:
            query = select(func.avg(cls.model.rate_mark).label('average_rate'),
                           func.count(cls.model.rate_mark).label('total_rates')).filter_by(product=product_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def get_most_rated_products(cls, limit: int=None):
        async with async_session_maker() as session:
            query = select(func.avg(cls.model.rate_mark).label('average_rate'),
                           func.count(cls.model.rate_mark).label('total_rates'),
                           cls.model.product).group_by(cls.model.product).order_by(desc('average_rate')).limit(limit)
            result = await session.execute(query)
            return result.mappings().all()