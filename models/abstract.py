import ipaddress as ip
from abc import ABC, abstractmethod
from models.channel import InputChannel, OutputChannel
from models.matrix import Matrix


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


class Processor(ABC):

    def __init__(self):
        self._ip_addr: ip.IPv4Address = ...
        self._port: int = ...
        self._system_mute: bool = ...
        self._scenes: list[str] = ...
        self._input: list[InputChannel] = ...
        self._output: list[OutputChannel] = ...
        self._matrix: Matrix = ...

    @property
    @abstractmethod
    def ip_addr(self) -> ip.IPv4Address:
        pass

    @ip_addr.setter
    @abstractmethod
    def ip_addr(self, ip_addr: ip.IPv4Address):
        pass

    @property
    @abstractmethod
    def port(self) -> int:
        pass

    @port.setter
    @abstractmethod
    def port(self, port: int):
        pass

    @property
    @abstractmethod
    def system_mute(self) -> bool:
        pass

    @system_mute.setter
    @abstractmethod
    def system_mute(self, mute: bool):
        pass

    @property
    @abstractmethod
    def scenes(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def input_channels(self) -> list[InputChannel]:
        pass

    @property
    @abstractmethod
    def output_channels(self) -> list[OutputChannel]:
        pass

    @property
    @abstractmethod
    def matrix(self) -> Matrix:
        pass
