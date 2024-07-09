from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self, number: int) -> None:
        if not isinstance(number, int):
            raise ValueError("Number must be an integer.")
        if not 0 <= number <= 63:
            raise ValueError("Channel number must be between 0 and 64.")

        self._number = number
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
