from abc import ABC, abstractmethod
from typing import List, Dict


class Matrix(ABC):
    def __init__(self, channels: int = 4) -> None:
        if not isinstance(channels, int):
            raise ValueError("Channels must be an integer.")
        if not 1 <= channels <= 64:
            raise ValueError("Channels can only be between 1 and 64.")

        self._channels = channels
        self._matrix = [[{"route": False, "gain": -120.0} for _ in range(channels)] for _ in range(channels)]

    @property
    def channels(self) -> int:
        return self._channels

    @property
    def matrix(self) -> List[List[Dict]]:
        return self._matrix

    def __str__(self, channels: int = None) -> str:
        if not isinstance(channels, int):
            raise ValueError("Channels must be an integer.")
        if not 1 <= channels <= self._channels:
            raise ValueError(f"Invalid channel {channels}. Must be between 1 and {self._channels}.")

        description = f"Matrix with {self._channels} channels:\n"
        for i in range(self._channels):
            line = f"[Channel {i+1}] "
            for j in range(self._channels):
                route = "Route: True" if self._matrix[i][j]["route"] else "Route: False"
                gain = f"Gain: {-self._matrix[i][j]['gain']} dB"
                line += f"{route} {gain} | "
            description += line + "\n"
        return description
