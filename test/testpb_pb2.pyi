from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZERO: _ClassVar[TestEnum]
    ONE: _ClassVar[TestEnum]
    TWO: _ClassVar[TestEnum]

ZERO: TestEnum
ONE: TestEnum
TWO: TestEnum

class TestMessage(_message.Message):
    __slots__ = (
        "bool",
        "bytes",
        "double",
        "fixed32",
        "fixed64",
        "float",
        "int32",
        "int64",
        "map",
        "nested",
        "self",
        "sint32",
        "sint64",
        "string",
        "strings",
        "test_enum",
        "uint32",
        "uint64",
    )
    class Nested(_message.Message):
        __slots__ = ("string",)
        STRING_FIELD_NUMBER: _ClassVar[int]
        string: str
        def __init__(self, string: str | None = ...) -> None: ...

    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: str | None = ..., value: int | None = ...) -> None: ...

    BOOL_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    TEST_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    int32: int
    int64: int
    uint32: int
    uint64: int
    sint32: int
    sint64: int
    fixed32: int
    fixed64: int
    float: float
    double: float
    string: str
    bytes: bytes
    test_enum: TestEnum
    nested: TestMessage.Nested
    strings: _containers.RepeatedScalarFieldContainer[str]
    map: _containers.ScalarMap[str, int]
    self: TestMessage
    def __init__(
        self_,
        bool: bool | None = ...,
        int32: int | None = ...,
        int64: int | None = ...,
        uint32: int | None = ...,
        uint64: int | None = ...,
        sint32: int | None = ...,
        sint64: int | None = ...,
        fixed32: int | None = ...,
        fixed64: int | None = ...,
        float: float | None = ...,
        double: float | None = ...,
        string: str | None = ...,
        bytes: bytes | None = ...,
        test_enum: TestEnum | str | None = ...,
        nested: TestMessage.Nested | _Mapping | None = ...,
        strings: _Iterable[str] | None = ...,
        map: _Mapping[str, int] | None = ...,
        self: TestMessage | _Mapping | None = ...,
    ) -> None: ...

class ExtendedTestMessage(_message.Message):
    __slots__ = (
        "bool",
        "bytes",
        "complex_other_message",
        "double",
        "fixed32",
        "fixed64",
        "float",
        "int32",
        "int64",
        "int_to_string_map",
        "message_map",
        "nested",
        "nested_nested_self",
        "nested_self",
        "nesteds",
        "self",
        "self_map",
        "selves",
        "sint32",
        "sint64",
        "string",
        "string_to_int_map",
        "strings",
        "test_enum",
        "uint32",
        "uint64",
    )
    class Nested(_message.Message):
        __slots__ = ("string",)
        STRING_FIELD_NUMBER: _ClassVar[int]
        string: str
        def __init__(self, string: str | None = ...) -> None: ...

    class NestedSelf(_message.Message):
        __slots__ = ("self",)
        SELF_FIELD_NUMBER: _ClassVar[int]
        self: ExtendedTestMessage
        def __init__(
            self_, self: ExtendedTestMessage | _Mapping | None = ...
        ) -> None: ...

    class NestedNestedSelf(_message.Message):
        __slots__ = ("nested_self",)
        NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
        nested_self: ExtendedTestMessage.NestedSelf
        def __init__(
            self, nested_self: ExtendedTestMessage.NestedSelf | _Mapping | None = ...
        ) -> None: ...

    class StringToIntMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: str | None = ..., value: int | None = ...) -> None: ...

    class IntToStringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: int | None = ..., value: str | None = ...) -> None: ...

    class MessageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExtendedTestMessage.Nested
        def __init__(
            self,
            key: str | None = ...,
            value: ExtendedTestMessage.Nested | _Mapping | None = ...,
        ) -> None: ...

    class SelfMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExtendedTestMessage
        def __init__(
            self,
            key: str | None = ...,
            value: ExtendedTestMessage | _Mapping | None = ...,
        ) -> None: ...

    BOOL_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    TEST_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    COMPLEX_OTHER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    NESTEDS_FIELD_NUMBER: _ClassVar[int]
    SELVES_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT_MAP_FIELD_NUMBER: _ClassVar[int]
    INT_TO_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
    NESTED_NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    int32: int
    int64: int
    uint32: int
    uint64: int
    sint32: int
    sint64: int
    fixed32: int
    fixed64: int
    float: float
    double: float
    string: str
    bytes: bytes
    test_enum: TestEnum
    nested: ExtendedTestMessage.Nested
    complex_other_message: TestMessage
    strings: _containers.RepeatedScalarFieldContainer[str]
    nesteds: _containers.RepeatedCompositeFieldContainer[ExtendedTestMessage.Nested]
    selves: _containers.RepeatedCompositeFieldContainer[ExtendedTestMessage]
    string_to_int_map: _containers.ScalarMap[str, int]
    int_to_string_map: _containers.ScalarMap[int, str]
    message_map: _containers.MessageMap[str, ExtendedTestMessage.Nested]
    self_map: _containers.MessageMap[str, ExtendedTestMessage]
    self: ExtendedTestMessage
    nested_self: ExtendedTestMessage.NestedSelf
    nested_nested_self: ExtendedTestMessage.NestedNestedSelf
    def __init__(
        self_,
        bool: bool | None = ...,
        int32: int | None = ...,
        int64: int | None = ...,
        uint32: int | None = ...,
        uint64: int | None = ...,
        sint32: int | None = ...,
        sint64: int | None = ...,
        fixed32: int | None = ...,
        fixed64: int | None = ...,
        float: float | None = ...,
        double: float | None = ...,
        string: str | None = ...,
        bytes: bytes | None = ...,
        test_enum: TestEnum | str | None = ...,
        nested: ExtendedTestMessage.Nested | _Mapping | None = ...,
        complex_other_message: TestMessage | _Mapping | None = ...,
        strings: _Iterable[str] | None = ...,
        nesteds: _Iterable[ExtendedTestMessage.Nested | _Mapping] | None = ...,
        selves: _Iterable[ExtendedTestMessage | _Mapping] | None = ...,
        string_to_int_map: _Mapping[str, int] | None = ...,
        int_to_string_map: _Mapping[int, str] | None = ...,
        message_map: _Mapping[str, ExtendedTestMessage.Nested] | None = ...,
        self_map: _Mapping[str, ExtendedTestMessage] | None = ...,
        self: ExtendedTestMessage | _Mapping | None = ...,
        nested_self: ExtendedTestMessage.NestedSelf | _Mapping | None = ...,
        nested_nested_self: ExtendedTestMessage.NestedNestedSelf
        | _Mapping
        | None = ...,
    ) -> None: ...
