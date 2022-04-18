from typing import Dict, Any, TypeVar, Generic
from marshmallow import Schema
from lib.dao import BaseDAO

T = TypeVar('T', bound=BaseDAO)


class BaseService(Generic[T]):

    def __init__(self, dao: T, schema: Schema):
        self.dao = dao
        self.schema = schema

    def qet_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        return self.schema.dump(self.dao.get_one(uid))

    def create(self, data: Dict[str, Any]):
        self.dao.create(self.schema.load(data))

    def update(self, uid: int, data: Dict[str, Any]):
        self.dao.update(uid, self.schema.load(data))

    def delete(self, uid: int):
        self.dao.delete(uid)
