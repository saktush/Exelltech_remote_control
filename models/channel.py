from abc import ABC, abstractmethod
from typing import Literal


class Channel(ABC):
    def __init__(self) -> None:
        self._number = 0
        self._name = ''
        self._mute = False
        self._gain = 0.0
        self._link = False
        self._level = -160.0

    @property
    def number(self) -> int:
        return self._number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) > 16:
            raise ValueError("Name length cannot exceed 16 characters.")
        for char in value:
            if not char.isascii():
                raise ValueError("Name can only contain ASCII letters and symbols.")
        self._name = value

    @property
    def mute(self) -> bool:
        return self._mute

    @mute.setter
    def mute(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Mute must be a boolean.")
        self._mute = value

    @property
    def gain(self) -> float:
        return self._gain

    @gain.setter
    def gain(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("Gain must be a float.")
        if not -72 <= value <= 12:
            raise ValueError("Gain must be between -72 and 12.")
        self._gain = value

    @property
    def link(self) -> bool:
        return self._link

    @link.setter
    def link(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Link must be a boolean.")
        self._link = value

    @property
    def level(self) -> float:
        return self._level

    def __str__(self) -> str:
        return (f"Channel {self.number}: {self.name} - Mute: {self.mute}, "
                f"Gain: {self.gain}, Linked: {self.link}, Level: {self.level}")


class InputChannel(Channel):
    def __init__(self, number: int, is_dante: bool = False, ) -> None:
        super().__init__()
        if not isinstance(number, int):
            raise ValueError("Number must be an integer.")
        if not 0 <= number <= 63:
            raise ValueError("Channel number must be between 0 and 64.")

        self._number = number
        self._name = f'IN{number + 1}'
        self._mute = False
        self._phantom_power = False
        self._gain = 0.0
        self._link = False
        self._level = -160.0
        self._sensitivity: int = 0
        self._source: Literal["input", "generator"] = "input"
        self._isdante: bool = is_dante
        self._phase: bool = False

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
    def isdante(self) -> bool:
        return self._isdante

    @property
    def sensitivity(self) -> int:
        if self._isdante:
            raise AttributeError("Dante channels has no sensitivity settings")
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, value: int) -> None:
        if self._isdante:
            raise AttributeError("Dante channels has no sensitivity settings")
        if not isinstance(value, int):
            raise ValueError("Sensitivity must be an integer.")
        if not 0 <= value <= 15:
            raise ValueError("Sensitivity can only be between 0 and 15.")
        self._sensitivity = value

    @property
    def phantom_power(self) -> bool:
        if self._isdante:
            raise AttributeError("Dante channels has no phantom power")
        return self._phantom_power

    @phantom_power.setter
    def phantom_power(self, value: bool) -> None:
        if self._isdante:
            raise AttributeError("Dante channels has no phantom power")
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
