from typing import Type

from graia.broadcast import Dispatchable
from pydantic import validator

from graia.ariadne.model import AriadneBaseModel

from ..dispatcher import ApplicationDispatcher
from ..exception import InvalidEventTypeDefinition


class MiraiEvent(Dispatchable, AriadneBaseModel):
    type: str

    @validator("type", allow_reuse=True)
    def validate_event_type(cls, v):
        if cls.type != v:
            raise InvalidEventTypeDefinition(
                "{0}'s type must be '{1}', not '{2}'".format(cls.__name__, cls.type, v)
            )
        return v

    class Config:
        extra = "ignore"

    Dispatcher = ApplicationDispatcher
