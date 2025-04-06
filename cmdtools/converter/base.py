from typing import TypeAlias, Type, Union

__all__ = [
    "BaseConverter",
    "BaseType",
    "BasicTypes",
]

BaseType: TypeAlias = Union[int, float, str, bool]
BasicTypes: TypeAlias = Type[BaseType]


class BaseConverter:
    """The converter base class"""

    def __init__(self, value: BaseType):
        self.value = value
