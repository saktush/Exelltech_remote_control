import logging
import time

from .abstract import Processor
from .api import ASCII as api
from .enums import SwitchState
from .exceptions import CommunicationError
from .system import UDP


class Driver:
    @staticmethod
    def _get_ascii(proc: Processor, command: str) -> str | None:
        try:
            response = UDP.send(proc.local_ip, proc.local_port, proc.ip_addr, proc.port, command)
            if response:
                return response[len(command) :]
        except (RuntimeError, OSError) as e:
            raise CommunicationError(f"Failed to send command '{command}': {e}") from e
        finally:
            time.sleep(0.005)
        return None

    @staticmethod
    def pull_input_channels_gain(proc: Processor) -> list[float] | None:
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
    def pull_output_channels_gain(proc: Processor) -> list[float] | None:
        command = api.get.output.gains(0, len(proc.output_channels))
        response_data = Driver._get_ascii(proc, command)
        if response_data:
            try:
                return [float(i) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channels_mute(proc: Processor) -> list[bool] | None:
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
    def pull_output_channels_mute(proc: Processor) -> list[bool] | None:
        command = api.get.output.mutes(0, len(proc.output_channels))
        response_data = Driver._get_ascii(proc, command)
        if response_data:
            try:
                return [bool(int(i)) for i in response_data.split("#")[1:]]
            except ValueError:
                logging.error(f"Failed to parse gains values: {response_data}")
                return None
        return None

    @staticmethod
    def pull_input_channels_level(proc: Processor) -> list[float] | None:
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
    def pull_output_channels_level(proc: Processor) -> list[float] | None:
        command = api.get.output.levels(0, len(proc.output_channels))
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
        for i in range(proc.matrix.inputs):
            command = api.get.mixer.switch_vertical(i, (0, proc.matrix.outputs))
            response_data = Driver._get_ascii(proc, command)
            if response_data:
                try:
                    values = [bool(int(v)) for v in response_data.split("#")[1:]]
                except ValueError:
                    logging.error(f"Failed to parse matrix switch row {i}: {response_data}")
                    continue
                for k, value in enumerate(values):
                    proc.matrix.set_route(i, k, value)

    @staticmethod
    def push_matrix_switches(proc: Processor) -> bool | None:
        all_ok = True
        for i, row in enumerate(proc.matrix.routes):
            for k, switch in enumerate(row):
                value = SwitchState.ON if switch else SwitchState.OFF
                command = api.set.mixer.switch(i, k, value)
                response_data = Driver._get_ascii(proc, command)
                if not response_data:
                    all_ok = False
        return all_ok
