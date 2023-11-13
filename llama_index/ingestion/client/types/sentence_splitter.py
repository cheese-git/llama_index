# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class SentenceSplitter(pydantic.BaseModel):
    """
    Parse text with a preference for complete sentences.

    In general, this class tries to keep sentences and paragraphs together. Therefore
    compared to the original TokenTextSplitter, there are less likely to be
    hanging sentences or parts of sentences at the end of the node chunk.
    """

    include_metadata: typing.Optional[bool] = pydantic.Field(
        description="Whether or not to consider metadata when splitting."
    )
    include_prev_next_rel: typing.Optional[bool] = pydantic.Field(
        description="Include prev/next node relationships."
    )
    callback_manager: typing.Optional[typing.Dict[str, typing.Any]]
    chunk_size: typing.Optional[int] = pydantic.Field(
        description="The token chunk size for each chunk."
    )
    chunk_overlap: typing.Optional[int] = pydantic.Field(
        description="The token overlap of each chunk when splitting."
    )
    separator: typing.Optional[str] = pydantic.Field(
        description="Default separator for splitting into words"
    )
    paragraph_separator: typing.Optional[str] = pydantic.Field(
        description="Separator between paragraphs."
    )
    secondary_chunking_regex: typing.Optional[str] = pydantic.Field(
        description="Backup regex for splitting into sentences."
    )
    class_name: typing.Optional[str]

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
