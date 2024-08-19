from abc import ABC

from fastapi import HTTPException, status


class BaseApiException(HTTPException, ABC):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class RateAlreadyExists(BaseApiException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Отзыв уже был оставлен! Второй отзыв оставить не получится'


class RateNotFound(BaseApiException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Отзыв не найден!'


class NotARateAuthor(BaseApiException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = 'Для изменения/удаления отзыва необходимо быть его автором'
