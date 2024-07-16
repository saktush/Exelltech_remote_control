import time
import logging
import ipaddress as ip
from abc import ABC, abstractmethod
from typing import Optional, List
from models.channel import InputChannel, OutputChannel
from models.matrix import Matrix
from models.api import ASCII as api
from models.system import UDP
from config import LOCAL_IP, LOCAL_PORT


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


class ChannelManager:
    @staticmethod
    def _send_and_parse(proc: Processor, command: str) -> Optional[str]:
        try:
            response = UDP.send(LOCAL_IP, LOCAL_PORT, proc.ip_addr, proc.port, command)
            if response:
                return response[len(command):]
        except Exception as e:
            logging.error(f"Error while sending command '{command}': {e}")
        finally:
            time.sleep(0.005)
        return None

    @staticmethod
    def pull_input_channels_gain(proc: Processor) -> Optional[List[float]]:
        command = api.get.input.gains(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_output_channels_gain(proc: Processor) -> Optional[List[float]]:
        command = api.get.output.gains(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channels_mute(proc: Processor) -> Optional[List[bool]]:
        command = api.get.input.mutes(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [bool(int(i)) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_output_channels_mute(proc: Processor) -> Optional[List[bool]]:
        command = api.get.output.mutes(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [bool(int(i)) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channels_level(proc: Processor) -> Optional[List[float]]:
        command = api.get.input.levels(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_output_channels_level(proc: Processor) -> Optional[List[float]]:
        command = api.get.output.levels(0, len(proc.input_channels))
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None


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
        self.__mgmt = ChannelManager()
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

    def pull_channels(self) -> None:
        input_gains: List[float] = self.__mgmt.pull_input_channels_gain(self)
        output_gains: List[float] = self.__mgmt.pull_output_channels_gain(self)
        input_mutes: List[bool] = self.__mgmt.pull_input_channels_mute(self)
        output_mutes: List[bool] = self.__mgmt.pull_output_channels_mute(self)
        input_levels: List[float] = self.__mgmt.pull_input_channels_level(self)
        output_levels: List[float] = self.__mgmt.pull_output_channels_level(self)

        # [Optional] Add more data to channel
        # self.input_channels[number].source = ...
        # self.input_channels[number].phase = ...
        # self.input_channels[number].name = ...
        # self.input_channels[number].link = ...

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
                o_ch.mutes = output_mutes[o_ch.number]
            if output_levels:
                o_ch.level = input_levels[o_ch.number]
