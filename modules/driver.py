import logging
import time
from typing import Optional, List, Literal
from config import LOCAL_IP, LOCAL_PORT
from modules.api import ASCII as api
from modules.abstract import Processor
from modules.system import UDP


class Driver:
    @staticmethod
    def _get_ascii(proc: Processor, command: str) -> Optional[str]:
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
        response_data = Driver._get_ascii(proc, command)
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
        response_data = Driver._get_ascii(proc, command)
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
        response_data = Driver._get_ascii(proc, command)
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
        response_data = Driver._get_ascii(proc, command)
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
        response_data = Driver._get_ascii(proc, command)
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
        response_data = Driver._get_ascii(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_matrix_switches(proc: Processor) -> None:
        for i, row in enumerate(proc.matrix.routes):
            for k, cell in enumerate(row):
                command = api.get.mixer.switch(i, k)
                response_data = Driver._get_ascii(proc, command)
                if response_data:
                    try:
                        value = bool(int(response_data))
                    except ValueError:
                        logging.error(f"Failed to parse matrix switch value: {response_data}")
                        continue
                    # set value
                    proc.matrix.set_route(i, k, value)

    @staticmethod
    def push_matrix_switches(proc: Processor) -> Optional[True]:
        for i, row in enumerate(proc.matrix.routes):
            for k, switch in enumerate(row):
                value: Literal[0, 1] = 1 if switch else 0
                command = api.set.mixer.switch(i, k, value)
                response_data = Driver._get_ascii(proc, command)
                if response_data:
                    return True

