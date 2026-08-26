import ipaddress as ip
from abc import ABC, abstractmethod
from collections.abc import Sequence

from .matrix import Matrix


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

    _number: int
    _name: str
    _mute: bool
    _gain: float
    _link: bool
    _level: float

    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def __repr__(self) -> str:
        return (
            f"Channel {self.number}: {self.name} - Mute: {self.mute}, "
            f"Gain: {self.gain}, Linked: {self.link}, Level: {self.level}"
        )

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
        if len(value) > 15:
            raise ValueError("Name length cannot exceed 15 characters.")
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


class Processor(ABC):
    _ip_addr: ip.IPv4Address
    _port: int
    _local_ip: ip.IPv4Address
    _local_port: int
    _system_mute: bool
    _scenes: list[str]
    _matrix: Matrix

    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def __repr__(self) -> str: ...

    @property
    @abstractmethod
    def ip_addr(self) -> ip.IPv4Address: ...

    @ip_addr.setter
    @abstractmethod
    def ip_addr(self, ip_addr: ip.IPv4Address) -> None: ...

    @property
    @abstractmethod
    def port(self) -> int: ...

    @port.setter
    @abstractmethod
    def port(self, port: int) -> None: ...

    @property
    @abstractmethod
    def local_ip(self) -> ip.IPv4Address: ...

    @property
    @abstractmethod
    def local_port(self) -> int: ...

    @property
    @abstractmethod
    def system_mute(self) -> bool: ...

    @system_mute.setter
    @abstractmethod
    def system_mute(self, mute: bool) -> None: ...

    @property
    @abstractmethod
    def scenes(self) -> list[str]: ...

    @property
    @abstractmethod
    def input_channels(self) -> Sequence[Channel]: ...

    @property
    @abstractmethod
    def output_channels(self) -> Sequence[Channel]: ...

    @property
    @abstractmethod
    def matrix(self) -> Matrix: ...
