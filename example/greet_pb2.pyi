from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Greeting(_message.Message):
    __slots__ = ("full_name", "known_name", "nickname")
    class KnownName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Greeting.KnownName]
        ALICE: _ClassVar[Greeting.KnownName]
        BOB: _ClassVar[Greeting.KnownName]

    UNKNOWN: Greeting.KnownName
    ALICE: Greeting.KnownName
    BOB: Greeting.KnownName
    class FullName(_message.Message):
        __slots__ = ("first_name", "last_name")
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        def __init__(
            self, first_name: str | None = ..., last_name: str | None = ...
        ) -> None: ...

    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    KNOWN_NAME_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    full_name: Greeting.FullName
    known_name: Greeting.KnownName
    def __init__(
        self,
        nickname: str | None = ...,
        full_name: Greeting.FullName | _Mapping | None = ...,
        known_name: Greeting.KnownName | str | None = ...,
    ) -> None: ...

class GreetingRequest(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: Greeting
    def __init__(self, greeting: Greeting | _Mapping | None = ...) -> None: ...

class GreetingResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: str | None = ...) -> None: ...
