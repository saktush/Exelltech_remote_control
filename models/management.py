import time
import logging
from typing import Callable, Optional, List
from models.api import ASCII as api
from models.system import UDP
from models.channel import InputChannel
from models.processor import Processor
from config import LOCAL_IP, LOCAL_PORT


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
    def pull_input_channel_gain(proc: Processor, channel: InputChannel) -> Optional[float]:
        command = api.get.input.gain(channel.number)
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return float(response_data.replace("#", ""))
            except ValueError:
                logging.error(f"Failed to parse gain value: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channels_gain(proc: Processor, start_ch: InputChannel,
                                 end_ch: InputChannel) -> Optional[List[float]]:
        command = api.get.input.gains(start_ch.number, end_ch.number)
        response_data = ChannelManager._send_and_parse(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channel_mute(proc: Processor, channel: InputChannel) -> bool | None:
        ...

    @staticmethod
    def pull_input_channel_level(proc: Processor, channel: InputChannel) -> float | None:
        ...
