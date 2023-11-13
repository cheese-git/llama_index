# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .configurable_data_sink_names import ConfigurableDataSinkNames
from .data_sink_component import DataSinkComponent


class DataSink(pydantic.BaseModel):
    """
    Schema for a data sink.
    """

    id: typing.Optional[str] = pydantic.Field(description="Unique identifier")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Creation datetime"
    )
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="Update datetime"
    )
    sink_type: ConfigurableDataSinkNames
    component: DataSinkComponent
    name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
