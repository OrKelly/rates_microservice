from typing import List

from fastapi import APIRouter, Depends, Query

from app.rates.dao import RatesDAO
from app.rates.dependency import valid_rate_id
from app.rates.exceptions import RateAlreadyExists, NotARateAuthor
from app.rates.schemas import SRate, RateUpdate, SCreateRate

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


@router.get('/product_rates_stat')
async def get_product_rates_stat(product_id: int = Query(description='Введите id продукта')):
    rates = await RatesDAO.get_product_rate_stat(product_id=product_id)
    return rates


@router.get('/most_rated')
async def get_most_rated_products(
        limit: int = Query(None, description='Введите число продуктов, которые необходимо вывести'
                                             '(по умолчанию будут выведены все)')):
    products = await RatesDAO.get_most_rated_products(limit=limit)
    return products


@router.get('/{rate_id}')
async def get_specified_rate(rate_id: int, rate=Depends(valid_rate_id)) -> SRate:
    return rate


@router.post('')
async def create_rate(rate: SCreateRate, user: int):
    existing_rate = await RatesDAO.find_one_or_none(user=user, product=rate.product)
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
