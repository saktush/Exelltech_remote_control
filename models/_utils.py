class ASCII:
    class get:
        class input:
            @staticmethod
            def gain(number: int):
                return f"get:input#gain#{number}"

            @staticmethod
            def gains(start: int, end: int):
                return f"get:input#gain#{start}-{end}"

    class set:
        class input:
            @staticmethod
            def gain(number: int, value: float):
                value = round(value, 2)
                return f"set:input#gain#{number}#{value}"

            @staticmethod
            def gains(start: int, end: int, value: float):
                value = round(value, 2)
                return f"set:input#gain#{start}-{end}#{value}"

