import ipaddress as ip

from .abstract import Processor
from .channel import InputChannel, OutputChannel
from .driver import Driver
from .matrix import Matrix


class ELTProcessor(Processor):
    def __init__(
        self,
        ip_addr: ip.IPv4Address | str,
        port: int,
        inputs: int,
        outputs: int,
        digital_from: int | None,
        local_ip: ip.IPv4Address | str = "0.0.0.0",
        local_port: int = 50000,
    ) -> None:
        """
        :param ip_addr: IPv4 address of the device.
        :param port: Port number of the device.
        :param inputs: Number of input channels.
        :param outputs: Number of output channels.
        :param local_ip: IPv4 address to bind the local UDP socket to when talking to the device.
        :param local_port: Port to bind the local UDP socket to when talking to the device.
        """
        self._ip_addr = ip.IPv4Address(ip_addr)
        self._port = port
        self._local_ip = ip.IPv4Address(local_ip)
        self._local_port = local_port
        self._system_mute = False
        self._scenes = [f"Preset {i}" for i in range(16)]
        self.__driver = Driver()
        if inputs < 1 or outputs < 1:
            raise ValueError(f"Inputs and outputs number should be positive int > 0, got {inputs}, {outputs}")
        if digital_from:
            input_channels: list[InputChannel] = [InputChannel(n) for n in range(digital_from)]
            input_channels.extend([InputChannel(n, is_digital=True) for n in range(digital_from, inputs)])
            output_channels: list[OutputChannel] = [OutputChannel(n) for n in range(digital_from)]
            output_channels.extend([OutputChannel(n, is_digital=True) for n in range(digital_from, outputs)])
        else:
            input_channels = [InputChannel(n) for n in range(inputs)]
            output_channels = [OutputChannel(n) for n in range(outputs)]

        self._input = input_channels
        self._output = output_channels
        self._matrix = Matrix(inputs, outputs)

    def __repr__(self) -> str:
        return (
            f"ELTProcessor(ip_addr={self._ip_addr}, port={self._port}, "
            f"system_mute={self._system_mute}, "
            f"inputs={len(self._input)}, outputs={len(self._output)})"
        )

    @property
    def ip_addr(self) -> ip.IPv4Address:
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr: ip.IPv4Address | str) -> None:
        try:
            self._ip_addr = ip.IPv4Address(ip_addr)
        except ValueError:
            raise ValueError(f"Invalid IP address: {ip_addr}") from None

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int) -> None:
        self._port = port

    @property
    def local_ip(self) -> ip.IPv4Address:
        return self._local_ip

    @property
    def local_port(self) -> int:
        return self._local_port

    @property
    def system_mute(self) -> bool:
        return self._system_mute

    @system_mute.setter
    def system_mute(self, mute: bool) -> None:
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

    def pull_channels(self) -> None:
        input_gains: list[float] | None = self.__driver.pull_input_channels_gain(self)
        output_gains: list[float] | None = self.__driver.pull_output_channels_gain(self)
        input_mutes: list[bool] | None = self.__driver.pull_input_channels_mute(self)
        output_mutes: list[bool] | None = self.__driver.pull_output_channels_mute(self)
        input_levels: list[float] | None = self.__driver.pull_input_channels_level(self)
        output_levels: list[float] | None = self.__driver.pull_output_channels_level(self)

        # [Optional] Add more data to channel
        # self.input_channels[number].source = ...
        # self.input_channels[number].phase = ...
        # self.input_channels[number].name = ...
        # self.input_channels[number].link = ...

        # TODO: check if channel numbers given correctly
        for i_ch in self.input_channels:
            if input_gains:
                i_ch.gain = input_gains[i_ch.number]
            if input_mutes:
                i_ch.mute = input_mutes[i_ch.number]
            if input_levels:
                i_ch.level = input_levels[i_ch.number]

        for o_ch in self.output_channels:
            if output_gains:
                o_ch.gain = output_gains[o_ch.number]
            if output_mutes:
                o_ch.mute = output_mutes[o_ch.number]
            if output_levels:
                o_ch.level = output_levels[o_ch.number]

    def pull_matrix(self) -> None:
        self.__driver.pull_matrix_switches(self)

    def push_matrix(self) -> bool | None:
        return self.__driver.push_matrix_switches(self)
