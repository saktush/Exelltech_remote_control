from abc import ABC, abstractmethod
from typing import List


class Matrix(ABC):
    MIN_GAIN = -120
    MAX_GAIN = 0

    def __init__(self, channels: int = 4) -> None:
        if not isinstance(channels, int):
            raise ValueError("Channels must be an integer.")
        if not 1 <= channels <= 64:
            raise ValueError("Channels can only be between 1 and 64.")

        self._channels = channels
        self._matrix_routes = [[False for _ in range(channels)] for _ in range(channels)]
        self._matrix_gains = [[-120.0 for _ in range(channels)] for _ in range(channels)]

    @property
    def channels(self) -> int:
        return self._channels

    @property
    def routes(self) -> List[List[bool]]:
        return self._matrix_routes

    @routes.setter
    def routes(self, value: List[List[bool]]) -> None:
        if not isinstance(value, list):
            raise ValueError("Matrix routes must be a list.")
        if len(value) != self._channels or any(len(row) != self._channels for row in value):
            raise ValueError(f"Invalid matrix routes. Must have {self._channels} rows and columns.")
        self._matrix_routes = value

    @property
    def gains(self) -> List[List[float]]:
        return self._matrix_gains

    @gains.setter
    def gains(self, value: List[List[float]]) -> None:
        if not isinstance(value, list):
            raise ValueError("Matrix gains must be a list.")
        if len(value) != self._channels or any(len(row) != self._channels for row in value):
            raise ValueError(f"Invalid matrix gains. Must have {self._channels} rows and columns.")
        for row in value:
            for gain in row:
                if not -120 <= gain <= 0:
                    raise ValueError(f"Gains must be between {self.MIN_GAIN} and {self.MAX_GAIN} dB.")
        self._matrix_gains = value

    def __str__(self) -> str:

        description = f"Matrix with {self._channels} channels:\n"
        for i in range(self._channels):
            line = f"[Channel {i + 1}] "
            for j in range(self._channels):
                route = "Route: True" if self._matrix_routes[i][j] else "Route: False"
                gain = f"Gain: {-self._matrix_gains[i][j]} dB"
                line += f"{route} {gain} | "
            description += line + "\n"
        return description
