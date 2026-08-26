from enum import Enum


class ChannelSource(str, Enum):
    INPUT = "input"
    GENERATOR = "generator"

    def __str__(self) -> str:
        return str(self.value)

    def __format__(self, format_spec: str) -> str:
        return format(self.value, format_spec)


class SwitchState(int, Enum):
    OFF = 0
    ON = 1

    def __str__(self) -> str:
        return str(int(self))

    def __format__(self, format_spec: str) -> str:
        return format(int(self), format_spec)
