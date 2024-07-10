from dataclasses import dataclass
from typing import Literal, AnyStr, Annotated


class ASCII:
    class get:
        class input:
            @staticmethod
            def gain(number: int) -> str:
                return f"get:input#gain#{number}"

            @staticmethod
            def gains(start: int, end: int) -> str:
                return f"get:input#gain#{start}-{end}"

            @staticmethod
            def phantom(number: int) -> str:
                return f"get:input#phant#{number}"

            @staticmethod
            def phantoms(start: int, end: int) -> str:
                return f"get:input#phant#{start}-{end}"

            @staticmethod
            def mute(number: int) -> str:
                return f"get:input#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int) -> str:
                return f"get:input#mute#{start}-{end}"

            @staticmethod
            def sensitivity(number: int) -> str:
                return f"get:input#sens#{number}"

            @staticmethod
            def sensitivities(start: int, end: int) -> str:
                return f"get:input#sens#{start}-{end}"

            @staticmethod
            def phase(number: int) -> str:
                return f"get:input#phase#{number}"

            @staticmethod
            def phases(start: int, end: int) -> str:
                return f"get:input#phase#{start}-{end}"

            @staticmethod
            def link(number: int) -> str:
                return f"get:input#link#{number}"

            @staticmethod
            def links(start: int, end: int) -> str:
                return f"get:input#link#{start}-{end}"

            @staticmethod
            def type(number: int) -> str:
                return f"get:input#type#{number}"

            @staticmethod
            def types(start: int, end: int) -> str:
                return f"get:input#type#{start}-{end}"

            @staticmethod
            def level(number: int) -> str:
                return f"get:input#level#{number}"

            @staticmethod
            def levels(start: int, end: int) -> str:
                return f"get:input#level#{start}-{end}"

        class output:
            @staticmethod
            def gain(number: int) -> str:
                return f"get:output#gain#{number}"

            @staticmethod
            def gains(start: int, end: int) -> str:
                return f"get:output#gain#{start}-{end}"

            @staticmethod
            def mute(number: int) -> str:
                return f"get:output#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int) -> str:
                return f"get:output#mute#{start}-{end}"

            @staticmethod
            def phase(number: int) -> str:
                return f"get:output#phase#{number}"

            @staticmethod
            def phases(start: int, end: int) -> str:
                return f"get:output#phase#{start}-{end}"

            @staticmethod
            def link(number: int) -> str:
                return f"get:output#link#{number}"

            @staticmethod
            def links(start: int, end: int) -> str:
                return f"get:output#link#{start}-{end}"

            @staticmethod
            def level(number: int) -> str:
                return f"get:output#level#{number}"

            @staticmethod
            def levels(start: int, end: int) -> str:
                return f"get:output#level#{start}-{end}"

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
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phase#{start}-{end}#{state}"

            @staticmethod
            def link(number: int, state: Literal[0, 1]) -> str:
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#link#{number}#{state}"

            @staticmethod
            def links(start: int, end: int, state: Literal[0, 1]) -> str:
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
                if value not in (0, 1):
                    raise ValueError("Value must be 0 or 1")
                return f"set:input#type#{start}-{end}#{value}"

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
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#link#{start}-{end}#{state}"

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

