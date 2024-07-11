import ipaddress as ip
from abc import ABC
from channel import InputChannel, OutputChannel
from matrix import Matrix


class Processor(ABC):

    def __init__(self):
        self._ip_addr: ip.IPv4Address = None
        self._port: int = None
        self._system_mute: bool = None
        self._scenes: list[str] = []
        self._input: list[InputChannel] = []
        self._output: list[OutputChannel] = []
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


class ELTProcessor(Processor):

    def __init__(self, ip_addr: ip.IPv4Address, port: int, inputs, outputs):
        """

        :param ip_addr:
        :param port:
        :param inputs:
        :param outputs:
        """
        super().__init__()
        self._ip_addr: ip.IPv4Address = ip_addr
        self._port: int = port
        self._system_mute: bool = False
        self._scenes: list[str] = []
        self._input: list[InputChannel] = [InputChannel(n) for n in range(inputs)]
        self._output: list[OutputChannel] = [OutputChannel(n) for n in range(outputs)]
        self._matrix: Matrix = Matrix(inputs, outputs)

    @property
    def ip_addr(self) -> ip.IPv4Address:
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr: ip.IPv4Address | str):
        try:
            self._ip_addr = ip.ip_address(ip_addr)
        except ValueError:
            pass

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int):
        self._port = port

    @property
    def system_mute(self) -> bool:
        return self._system_mute

    @system_mute.setter
    def system_mute(self, mute: bool):
        self._system_mute = mute

    @property
    def scenes(self) -> list[str]:
        return self._scenes

    @property
    def input_channels(self) -> list[InputChannel]:
        return self._input

    @property
    def output_channels(self) -> list[OutputChannel]:
        return self._output

    @property
    def matrix(self) -> Matrix:
        return self._matrix
