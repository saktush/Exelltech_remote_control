import logging
from typing import Optional
from models.api import ASCII as api
from models.system import UDP
from models.channel import InputChannel, OutputChannel
from models.processor import Processor, ELTProcessor
from config import LOCAL_IP, LOCAL_PORT


class ChannelManager:
    @staticmethod
    def _send_command(proc: Processor, command: str) -> Optional[str]:
        try:
            response = UDP.send(proc.ip_addr, proc.port, LOCAL_IP, LOCAL_PORT, command)
            if response:
                data = response[len(command):]
                return data
        except Exception as e:
            logging.error(f"Error sending command '{command}': {e}")
            return None

    @staticmethod
    def get_input_channel_gain(proc: Processor, channel: InputChannel) -> Optional[str]:
        command = api.get.input.gain(channel.number)
        return ChannelManager._send_command(proc, command)

    @staticmethod
    def get_output_channel_gain(proc: Processor, channel: OutputChannel) -> Optional[str]:
        command = api.get.output.gain(channel.number)
        return ChannelManager._send_command(proc, command)
