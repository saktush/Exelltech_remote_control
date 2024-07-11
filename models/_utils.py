from typing import Literal, AnyStr, Annotated


class ASCII:
    """
    *A class that provides methods for handling various ASCII commands for matrix audio processor.*

    Structure:

    - ASCII.scene: Static methods for saving and toggling scenes.
    - ASCII.get: Nested classes with static methods for fetching system, scene, input, output, and mixer properties.
        - ASCII.get.sysctl: System control commands.
        - ASCII.get.scene: Scene-related commands.
        - ASCII.get.input: Input-related commands.
        - ASCII.get.output: Output-related commands.
        - ASCII.get.mixer: Mixer-related commands.

    - ASCII.set: Nested classes with static methods for setting system, scene, input, output, and mixer properties.
        - ASCII.set.sysctl: System control commands.
        - ASCII.set.scene: Scene-related commands.
        - ASCII.set.input: Input-related commands.
        - ASCII.set.output: Output-related commands.
        - ASCII.set.mixer: Mixer-related commands.
    """

    class scene:
        """
        A class for handling scene save and toggle operations.

        Methods:
        - save(scene_number: int) -> str: Save the specified scene number.
        - toggle(scene_number: int) -> str: Toggle the specified scene number.
        """

        @staticmethod
        def save(scene_number: int) -> str:
            if not (0 <= scene_number <= 15):
                raise ValueError("Scene number must be between 0 and 15")
            return f"scene:save#{scene_number}"

        @staticmethod
        def toggle(scene_number: int) -> str:
            if not (0 <= scene_number <= 15):
                raise ValueError("Scene number must be between 0 and 15")
            return f"scene:toggle#{scene_number}"

    class get:
        """
        *A class for handling various 'get' commands.*

        Structure:

        - sysctl: Contains system control commands like mute.
        - scene: Includes commands for fetching scene names and ranges.
        - input: Provides commands for retrieving input parameters like gain, phantom power, mute, sensitivity, phase, link, type, level, and name.
        - output: Contains commands for fetching output parameters like gain, mute, phase, link, level, and name.
        - mixer: Includes commands for retrieving mixer parameters like switch and gain, both for specific rows and ranges.
        """
        class sysctl:
            @staticmethod
            def mute() -> str:
                return "get:sysctl#mute"

        class scene:
            @staticmethod
            def name(number: int) -> str:
                if number > 15:
                    raise ValueError("Scene number should be 0 to 15")
                return f"get:scene#name#{number}"

            @staticmethod
            def names(start: int, end: int) -> str:
                if end > 15:
                    raise ValueError("Scene max number should be 1 to 15")
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:scene#name#{start}-{end}"

        class input:
            @staticmethod
            def gain(number: int) -> str:
                return f"get:input#gain#{number}"

            @staticmethod
            def gains(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#gain#{start}-{end}"

            @staticmethod
            def phantom(number: int) -> str:
                return f"get:input#phant#{number}"

            @staticmethod
            def phantoms(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#phant#{start}-{end}"

            @staticmethod
            def mute(number: int) -> str:
                return f"get:input#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#mute#{start}-{end}"

            @staticmethod
            def sensitivity(number: int) -> str:
                return f"get:input#sens#{number}"

            @staticmethod
            def sensitivities(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#sens#{start}-{end}"

            @staticmethod
            def phase(number: int) -> str:
                return f"get:input#phase#{number}"

            @staticmethod
            def phases(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#phase#{start}-{end}"

            @staticmethod
            def link(number: int) -> str:
                return f"get:input#link#{number}"

            @staticmethod
            def links(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#link#{start}-{end}"

            @staticmethod
            def type(number: int) -> str:
                return f"get:input#type#{number}"

            @staticmethod
            def types(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#type#{start}-{end}"

            @staticmethod
            def level(number: int) -> str:
                return f"get:input#level#{number}"

            @staticmethod
            def levels(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#level#{start}-{end}"

            @staticmethod
            def name(number: int) -> str:
                return f"get:input#name#{number}"

            @staticmethod
            def names(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:input#name#{start}-{end}"

        class output:
            @staticmethod
            def gain(number: int) -> str:
                return f"get:output#gain#{number}"

            @staticmethod
            def gains(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#gain#{start}-{end}"

            @staticmethod
            def mute(number: int) -> str:
                return f"get:output#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#mute#{start}-{end}"

            @staticmethod
            def phase(number: int) -> str:
                return f"get:output#phase#{number}"

            @staticmethod
            def phases(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#phase#{start}-{end}"

            @staticmethod
            def link(number: int) -> str:
                return f"get:output#link#{number}"

            @staticmethod
            def links(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#link#{start}-{end}"

            @staticmethod
            def level(number: int) -> str:
                return f"get:output#level#{number}"

            @staticmethod
            def levels(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#level#{start}-{end}"

            @staticmethod
            def name(number: int) -> str:
                return f"get:output#name#{number}"

            @staticmethod
            def names(start: int, end: int) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"get:output#name#{start}-{end}"

        class mixer:
            @staticmethod
            def switch(row: int, col: int) -> str:
                return f"get:mixer#switch#{row}#{col}"

            @staticmethod
            def switch_vertical(row: int, col_range: tuple[int, int]) -> str:
                if col_range[0] >= col_range[1]:
                    raise ValueError("col_range Should have first int lower than second int")
                return f"get:mixer#switch#{row}#{col_range[0]}-{col_range[1]}"

            @staticmethod
            def switch_horizontal(row_range: tuple[int, int], col: int) -> str:
                if row_range[0] >= row_range[1]:
                    raise ValueError("row_range Should have first int lower than second int")
                return f"get:mixer#switch#{row_range[0]}-{row_range[1]}#{col}"

            @staticmethod
            def gain(row: int, col: int) -> str:
                return f"get:mixer#gain#{row}#{col}"

            @staticmethod
            def gain_vertical(row: int, col_range: tuple[int, int]) -> str:
                if col_range[0] >= col_range[1]:
                    raise ValueError("col_range Should have first int lower than second int")
                return f"get:mixer#gain#{row}#{col_range[0]}-{col_range[1]}"

            @staticmethod
            def gain_horizontal(row_range: tuple[int, int], col: int) -> str:
                if row_range[0] >= row_range[1]:
                    raise ValueError("row_range Should have first int lower than second int")
                return f"get:mixer#gain#{row_range[0]}-{row_range[1]}#{col}"

    class set:
        """
        *A class for handling various 'set' commands.*

        Static Methods:

        - rescene(): Clears all scene data.
        - refactory(): Performs a factory reset, including IP address and other settings.

        Structure:

        - sysctl: Contains system control commands such as mute.
        - scene: Includes commands for setting scene names and ranges.
        - input: Provides commands for setting input parameters like gain, phantom power, mute, sensitivity, phase, link, type, and name.
        - output: Contains commands for setting output parameters like gain, mute, phase, link, and name.
        - mixer: Includes commands for setting mixer parameters like switch and gain, both for specific rows and ranges.
        """
        @staticmethod
        def rescene():
            """!!! Clears all scene data"""
            return "set:rescene"

        @staticmethod
        def refactory():
            """!!! Factory reset, including ip address and other settings"""
            return "set:refactory"

        class sysctl:
            @staticmethod
            def mute(state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:sysctl#mute#{state}"

        class scene:
            @staticmethod
            def name(number: int, name: str) -> str:
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                return f"set:scene#name#{number}#{name}"

            @staticmethod
            def names(start: int, end: int, name: str) -> str:
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"set:scene#name#{start}-{end}#{name}"

        class input:
            @staticmethod
            def gain(number: int, value: float) -> str:
                """Value should be from -72 to 12"""
                if not (-72 <= value <= 12):
                    raise ValueError("Gain parameter should be from -72 to 12")
                value = round(value, 2)
                return f"set:input#gain#{number}#{value}"

            @staticmethod
            def gains(start: int, end: int, value: float) -> str:
                """Value should be from -72 to 12"""
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if not (-72 <= value <= 12):
                    raise ValueError("Gain parameter should be from -72 to 12")
                value = round(value, 2)
                return f"set:input#gain#{start}-{end}#{value}"

            @staticmethod
            def phantom(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phant#{number}#{state}"

            @staticmethod
            def phantoms(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phant#{start}-{end}#{state}"

            @staticmethod
            def mute(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#mute#{number}#{state}"

            @staticmethod
            def mutes(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#mute#{start}-{end}#{state}"

            @staticmethod
            def sensitivity(number: int, value: int) -> str:
                """Value is expected to be between 0 and 15"""
                if not (0 <= value <= 15):
                    raise ValueError("Value must be between 0 and 15")
                return f"set:input#sens#{number}#{value}"

            @staticmethod
            def sensitivities(start: int, end: int, value: int) -> str:
                """Value is expected to be between 0 and 15"""
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if not (0 <= value <= 15):
                    raise ValueError("Value must be between 0 and 15")
                return f"set:input#sens#{start}-{end}#{value}"

            @staticmethod
            def phase(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phase#{number}#{state}"

            @staticmethod
            def phases(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phase#{start}-{end}#{state}"

            @staticmethod
            def link(number: int, state: Literal[0, 1]) -> str:
                """
                Link affects odd to even both channels,
                if call  .link(number=0, state=1) -> it will also affect channel(1)
                """
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#link#{number}#{state}"

            @staticmethod
            def links(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#link#{start}-{end}#{state}"

            @staticmethod
            def type(number: int, value: Literal[0, 1]) -> str:
                if value not in (0, 1):
                    raise ValueError("Value must be 0 or 1")
                return f"set:input#type#{number}#{value}"

            @staticmethod
            def types(start: int, end: int, value: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if value not in (0, 1):
                    raise ValueError("Value must be 0 or 1")
                return f"set:input#type#{start}-{end}#{value}"

            @staticmethod
            def name(number: int, name: str) -> str:
                """Name should be ASCII, max 15 symbols"""
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                return f"set:input#name#{number}#{name}"

            @staticmethod
            def names(start: int, end: int, name: str) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"set:input#name#{start}-{end}#{name}"

        class output:
            @staticmethod
            def gain(number: int, value: float) -> str:
                """Value should be from -72 to 12"""
                if not (-72 <= value <= 12):
                    raise ValueError("Gain parameter should be from -72 to 12")
                value = round(value, 2)
                return f"set:output#gain#{number}#{value}"

            @staticmethod
            def gains(start: int, end: int, value: float) -> str:
                """Value should be from -72 to 12"""
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if not (-72 <= value <= 12):
                    raise ValueError("Gain parameter should be from -72 to 12")
                value = round(value, 2)
                return f"set:output#gain#{start}-{end}#{value}"

            @staticmethod
            def mute(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#mute#{number}#{state}"

            @staticmethod
            def mutes(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#mute#{start}-{end}#{state}"

            @staticmethod
            def phase(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#phase#{number}#{state}"

            @staticmethod
            def phases(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#phase#{start}-{end}#{state}"

            @staticmethod
            def link(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#link#{number}#{state}"

            @staticmethod
            def links(start: int, end: int, state: Literal[0, 1]) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#link#{start}-{end}#{state}"

            @staticmethod
            def name(number: int, name: str) -> str:
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                return f"set:output#name#{number}#{name}"

            @staticmethod
            def names(start: int, end: int, name: str) -> str:
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                if len(name) > 15:
                    raise ValueError("Name should be 15 symbols maximum")
                if not name.isascii():
                    raise ValueError("Name should be ASCII")
                if start >= end:
                    raise ValueError("Start argument should be lower than End")
                return f"set:output#name#{start}-{end}#{name}"

        class mixer:
            @staticmethod
            def switch(row: int, col: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:mixer#switch#{row}#{col}#{state}"

            @staticmethod
            def switch_vertical(row: int, col_range: tuple[int, int], state: Literal[0, 1]) -> str:
                if col_range[0] >= col_range[1]:
                    raise ValueError("col_range should have the first int lower than the second int")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:mixer#switch#{row}#{col_range[0]}-{col_range[1]}#{state}"

            @staticmethod
            def switch_horizontal(row_range: tuple[int, int], col: int, state: Literal[0, 1]) -> str:
                if row_range[0] >= row_range[1]:
                    raise ValueError("row_range should have the first int lower than the second int")
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:mixer#switch#{row_range[0]}-{row_range[1]}#{col}#{state}"

            @staticmethod
            def gain(row: int, col: int, value: float) -> str:
                value = round(value, 2)
                return f"set:mixer#gain#{row}#{col}#{value}"

            @staticmethod
            def gain_vertical(row: int, col_range: tuple[int, int], value: float) -> str:
                if col_range[0] >= col_range[1]:
                    raise ValueError("col_range should have the first int lower than the second int")
                value = round(value, 2)
                return f"set:mixer#gain#{row}#{col_range[0]}-{col_range[1]}#{value}"

            @staticmethod
            def gain_horizontal(row_range: tuple[int, int], col: int, value: float) -> str:
                if row_range[0] >= row_range[1]:
                    raise ValueError("row_range should have the first int lower than the second int")
                value = round(value, 2)
                return f"set:mixer#gain#{row_range[0]}-{row_range[1]}#{col}#{value}"
