from abc import ABC, abstractmethod
from typing import Literal


class Channel(ABC):
    """
    Abstract base class representing a channel in an audio system.

    This class provides attributes and methods for working with channels, including their number, name,
    mute status, gain level, linking state, and audio level. The properties can be accessed and set
    using getter and setter methods.

    Property:
        number: Gets the channel's number.
        name: Gets or sets the channel's name.
        mute: Gets or sets whether the channel is muted.
        gain: Gets or sets the channel's gain level.
        link: Gets or sets whether the channel is linked to another channel.
        level: Gets the channel's current audio level.

    Notes:
        The class provides a __str__ method for generating a human-readable string representation of
        the channel. This can be useful for debugging and logging purposes.

    Raises:
        ValueError: If an invalid value is passed when setting the name, mute, gain, or link properties.
    """
    MIN_GAIN = -72
    MAX_GAIN = 12
    MIN_LEVEL = -160
    MAX_LEVEL = 0

    def __init__(self) -> None:
        self._number = 0
        self._name = ''
        self._mute = False
        self._gain = 0.0
        self._link = False
        self._level: float = self.MIN_LEVEL

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
        if not self.MIN_GAIN <= value <= self.MAX_GAIN:
            raise ValueError(f"Gain must be between {self.MIN_GAIN} and {self.MAX_GAIN}.")
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
    def __init__(self, number: int, is_digital: bool = False) -> None:
        super().__init__()
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
        super().__init__()
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
