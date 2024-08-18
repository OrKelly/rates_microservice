from app.base_dao.dao import BaseDAO
from app.rates.models import Rate


class RatesDAO(BaseDAO):
    model = Rate
