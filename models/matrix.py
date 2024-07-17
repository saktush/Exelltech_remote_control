from typing import List


class Matrix:
    MIN_GAIN = -120
    MAX_GAIN = 0

    def __init__(self, input_channels: int, output_channels: int) -> None:
        if not isinstance(input_channels, int) or not isinstance(output_channels, int):
            raise ValueError("Input and Output channels must be integers.")
        if not 1 <= input_channels <= 64 or not 1 <= output_channels <= 64:
            raise ValueError("Input and Output channels can only be between 1 and 64.")

        self._input_channels = input_channels
        self._output_channels = output_channels
        self._matrix_routes = [[False for _ in range(output_channels)] for _ in range(input_channels)]
        self._matrix_gains = [[-120.0 for _ in range(output_channels)] for _ in range(input_channels)]

    @property
    def inputs(self) -> int:
        return self._input_channels

    @property
    def outputs(self) -> int:
        return self._output_channels

    @property
    def routes(self) -> List[List[bool]]:
        return self._matrix_routes

    @routes.setter
    def routes(self, value: List[List[bool]]) -> None:
        if not isinstance(value, list):
            raise ValueError("Matrix routes must be a list.")
        if len(value) != self._input_channels or any(len(row) != self._output_channels for row in value):
            raise ValueError(
                f"Invalid matrix routes. Must have {self._input_channels} rows and {self._output_channels} columns.")
        self._matrix_routes = value

    @property
    def gains(self) -> List[List[float]]:
        return self._matrix_gains

    @gains.setter
    def gains(self, value: List[List[float]]) -> None:
        if not isinstance(value, list):
            raise ValueError("Matrix gains must be a list.")
        if len(value) != self._input_channels or any(len(row) != self._output_channels for row in value):
            raise ValueError(
                f"Invalid matrix gains. Must have {self._input_channels} rows and {self._output_channels} columns.")
        for row in value:
            for gain in row:
                if not self.MIN_GAIN <= gain <= self.MAX_GAIN:
                    raise ValueError(f"Gains must be between {self.MIN_GAIN} and {self.MAX_GAIN} dB.")
        self._matrix_gains = value

    def set_route(self, row: int, col: int, value: bool) -> None:
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column indices must be integers.")
        if not (0 <= row < self._input_channels) or not (0 <= col < self._output_channels):
            raise ValueError(f"Row and column indices must be between 0 and input/output channels.")
        if not isinstance(value, bool):
            raise ValueError("Route value must be a boolean.")
        self._matrix_routes[row][col] = value

    def get_route(self, row: int, col: int) -> bool:
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column indices must be integers.")
        if not (0 <= row < self._input_channels) or not (0 <= col < self._output_channels):
            raise ValueError(f"Row and column indices must be between 0 and input/output channels.")
        return self._matrix_routes[row][col]

    def set_gain(self, row: int, col: int, value: float) -> None:
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column indices must be integers.")
        if not (0 <= row < self._input_channels) or not (0 <= col < self._output_channels):
            raise ValueError(f"Row and column indices must be between 0 and input/output channels.")
        if not (self.MIN_GAIN <= value <= self.MAX_GAIN):
            raise ValueError(f"Gain value must be between {self.MIN_GAIN} and {self.MAX_GAIN} dB.")
        self._matrix_gains[row][col] = value

    def get_gain(self, row: int, col: int) -> float:
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("Row and column indices must be integers.")
        if not (0 <= row < self._input_channels) or not (0 <= col < self._output_channels):
            raise ValueError(f"Row and column indices must be between 0 and input/output channels.")
        return self._matrix_gains[row][col]

    def __repr__(self) -> str:
        description = (f"Matrix with {self._input_channels} input channels "
                       f"and {self._output_channels} output channels:\n")
        for i in range(self._input_channels):
            line = f"[Input Channel {i + 1}] "
            for j in range(self._output_channels):
                route = "Route: True" if self._matrix_routes[i][j] else "Route: False"
                gain = f"Gain: {-self._matrix_gains[i][j]} dB"
                line += f"{route} {gain} | "
            description += line + "\n"
        return description
