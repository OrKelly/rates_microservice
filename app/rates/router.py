from typing import List

from fastapi import APIRouter, Depends, Query

from app.rates.dao import RatesDAO
from app.rates.dependency import valid_rate_id
from app.rates.exceptions import RateAlreadyExists, NotARateAuthor
from app.rates.schemas import SRate, RateUpdate

router = APIRouter(
    prefix='/rates',
    tags=['Rates'],
)


@router.get('')
async def get_rates(
        product: int = Query(None, description='Введите id продукта'),
        mark: str = Query(None, description='Введите оценку для фильтрации'),
        user: int = Query(None, description='Введите автора оценки')) -> List[SRate]:
    rates = await RatesDAO.find_all(product=product, rate_mark=mark, user=user)
    return rates


@router.get('/{rate_id}')
async def get_specified_rate(rate_id: int, rate=Depends(valid_rate_id)) -> SRate:
    return rate


@router.post('')
async def create_rate(rate: SRate, user: int):
    existing_rate = await RatesDAO.find_one_or_none(user=rate.user, product=rate.product)
    if existing_rate:
        raise RateAlreadyExists
    await RatesDAO.add(user=user, product=rate.product, rate_mark=rate.rate_mark,
                       comment=rate.comment)
    return {'success': True, 'data': 'Отзыв был успешно добавлен!'}


@router.put('/{rate_id}')
async def update_rate(rate: RateUpdate, rate_id: int, user: int, existing_rate=Depends(valid_rate_id)):
    if user != existing_rate.user:
        raise NotARateAuthor
    await RatesDAO.update(instance_id=existing_rate.id, rate_mark=rate.rate_mark,
                          comment=rate.comment)
    return {'success': True, 'data': 'Отзыв был успешно обновлен!'}


@router.delete('/{rate_id}')
async def delete_rate(rate_id: int, user: int, existing_rate=Depends(valid_rate_id)):
    if user != existing_rate.user:
        raise NotARateAuthor
    await RatesDAO.delete(instance_id=existing_rate.id)
    return {'success': True, 'data': 'Отзыв был успешно удален!'}
