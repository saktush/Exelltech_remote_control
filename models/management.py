import logging
import time
from typing import Optional, List
from config import LOCAL_IP, LOCAL_PORT
from models.api import ASCII as api
from models.abstract import Processor
from models.system import UDP


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
