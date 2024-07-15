import ipaddress as ip
from abc import ABC, abstractmethod
from typing import Optional
from models.channel import InputChannel, OutputChannel
from models.matrix import Matrix
from models.management import ChannelManager


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

    def __init__(self, ip_addr: ip.IPv4Address | str, port: int,
                 inputs: int, outputs: int,
                 digital_from: Optional[int]):
        """
        :param ip_addr: IPv4 address.
        :param port: Port number.
        :param inputs: Number of input channels.
        :param outputs: Number of output channels.
        """
        super().__init__()
        self._ip_addr: ip.IPv4Address = ip.ip_address(ip_addr)
        self._port: int = port
        self._system_mute: bool = False
        self._scenes: list[str] = [f"Preset {i}" for i in range(16)]
        if inputs < 1 or outputs < 1:
            raise ValueError(f"Inputs and outputs number should be positive int > 0, got {inputs}, {outputs}")
        if digital_from:
            self._input: list[InputChannel] = [InputChannel(n) for n in range(digital_from)]
            self._input.extend([InputChannel(n, is_digital=True) for n in range(digital_from, inputs)])
            self._output: list[OutputChannel] = [OutputChannel(n) for n in range(digital_from)]
            self._output.extend([OutputChannel(n, is_digital=True) for n in range(digital_from, outputs)])
        else:
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
            raise ValueError(f"Invalid IP address: {ip_addr}")

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

    def pull_input_channel(self, number: int) -> None:
        if not self.input_channels[number].is_digital:
            self.input_channels[number].phantom_power = ...
            self.input_channels[number].sensitivity = ...
        self.input_channels[number].mute = ...
        self.input_channels[number].gain = ...
        self.input_channels[number].level = ...
        self.input_channels[number].source = ...
        self.input_channels[number].phase = ...
        self.input_channels[number].name = ...
        self.input_channels[number].link = ...

    def pull_output_channel(self, number: int) -> None:
        self.output_channels[number].mute = ...
        self.output_channels[number].gain = ...
        self.output_channels[number].level = ...
        self.output_channels[number].name = ...
        self.output_channels[number].gain = ...

    def pull_matrix(self, number: int) -> None:
        self.matrix.routes = ...
        self.matrix.gains = ...
