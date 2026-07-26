from abc import ABC

from modules.abstract import Channel
from typing import Literal


class InputChannel(Channel):
    def __init__(self, number: int, is_digital: bool = False) -> None:
        if not isinstance(number, int):
            raise ValueError("Number must be an integer.")
        if not 0 <= number <= 63:
            raise ValueError("Channel number must be between 0 and 64.")
        if not isinstance(is_digital, bool):
            raise ValueError("is_digital parameter must be a boolean")

        self._number = number
        self._is_digital: bool = is_digital
        self._name = f'IN{number + 1}'
        self._mute = False
        self._phantom_power = False
        self._gain = 0.0
        self._link = False
        self._level = self.MIN_LEVEL
        self._sensitivity: int = 0
        self._source: Literal["input", "generator"] = "input"
        self._phase: bool = False

    def __repr__(self):
        return (
            f"InputChannel(number={self._number:02}, "
            f"is_digital={self._is_digital}, "
            f"name='{self._name}', "
            f"mute={self._mute}, "
            f"phantom_power={self._phantom_power}, "
            f"gain={self._gain}, "
            f"link={self._link}, "
            f"level={self._level}, "
            f"sensitivity={self._sensitivity}, "
            f"source='{self._source}', "
            f"phase={self._phase})"
        )

    @property
    def source(self) -> str:
        return self._source

    @source.setter
    def source(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Source must be a string.")
        if value not in ["input", "generator"]:
            raise ValueError("Source can only be 'input' or 'generator'.")
        self._source = value

    @property
    def is_digital(self) -> bool:
        return self._is_digital

    @property
    def sensitivity(self) -> int:
        if self._is_digital:
            raise AttributeError("digital channel has no sensitivity settings")
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, value: int) -> None:
        if self._is_digital:
            raise AttributeError("digital channels has no sensitivity settings")
        if not isinstance(value, int):
            raise ValueError("Sensitivity must be an integer.")
        if not 0 <= value <= 15:
            raise ValueError("Sensitivity can only be between 0 and 15.")
        self._sensitivity = value

    @property
    def phantom_power(self) -> bool:
        if self._is_digital:
            raise AttributeError("digital channels has no phantom power")
        return self._phantom_power

    @phantom_power.setter
    def phantom_power(self, value: bool) -> None:
        if self._is_digital:
            raise AttributeError("digital channels has no phantom power")
        if not isinstance(value, bool):
            raise ValueError("Phantom power must be a boolean.")
        self._phantom_power = value

    @property
    def phase(self) -> bool:
        return self._phase

    @phase.setter
    def phase(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Phase must be a boolean.")
        self._phase = value

    @property
    def level(self) -> float:
        return self._level

    @level.setter
    def level(self, value):
        self._level = value


class OutputChannel(Channel):
    def __init__(self, number: int, is_digital: bool = False, ) -> None:
        if not isinstance(number, int):
            raise ValueError("Number must be an integer.")
        if not 0 <= number <= 63:
            raise ValueError("Channel number must be between 0 and 64.")
        if not isinstance(is_digital, bool):
            raise ValueError("is_digital parameter must be a boolean")

        self._number = number
        self._name = f'OUT{number + 1}'
        self._is_digital: bool = is_digital
        self._mute = False
        self._gain = 0.0
        self._link = False
        self._level = self.MIN_LEVEL
        self._phase: bool = False

    def __repr__(self):
        return (
            f"InputChannel(number={self._number:02}, "
            f"is_digital={self._is_digital}, "
            f"name='{self._name}', "
            f"mute={self._mute}, "
            f"gain={self._gain}, "
            f"link={self._link}, "
            f"level={self._level}, "
            f"phase={self._phase})"
        )

    @property
    def phase(self) -> bool:
        return self._phase

    @phase.setter
    def phase(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Phase must be a boolean.")
        self._phase = value

    @property
    def is_digital(self) -> bool:
        return self._is_digital

    @property
    def level(self) -> float:
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
