import ipaddress as ip
from abc import ABC, abstractmethod
from channel import InputChannel, OutputChannel
from matrix import Matrix


class Processor(ABC):

    def __init__(self):
        self._ip_addr: ip.IPv4Address = None
        self._port: int = None
        self._system_mute: bool = None
        self._scenes: list[str] = []
        self._input_channels: list[InputChannel] = []
        self._output_channels: list[OutputChannel] = []
        self._matrix: Matrix = None

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

    @scenes.setter
    @abstractmethod
    def scenes(self, name: str):
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
