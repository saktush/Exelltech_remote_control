class ASCII:
    class get:
        class input:
            @staticmethod
            def gain(number: int):
                return f"get:input#gain#{number}"

            @staticmethod
            def gains(start: int, end: int):
                return f"get:input#gain#{start}-{end}"

            @staticmethod
            def phantom(number: int):
                return f"get:input#phant#{number}"

            @staticmethod
            def phantoms(start: int, end: int):
                return f"get:input#phant#{start}-{end}"

            @staticmethod
            def mute(number: int):
                return f"get:input#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int):
                return f"get:input#mute#{start}-{end}"

        class output:
            @staticmethod
            def gain(number: int):
                return f"get:output#gain#{number}"

            @staticmethod
            def gains(start: int, end: int):
                return f"get:output#gain#{start}-{end}"

            @staticmethod
            def mute(number: int):
                return f"get:output#mute#{number}"

            @staticmethod
            def mutes(start: int, end: int):
                return f"get:output#mute#{start}-{end}"

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

            @staticmethod
            def phantom(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phant#{number}#{state}"

            @staticmethod
            def phantoms(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phant#{start}-{end}#{state}"

            @staticmethod
            def mute(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#mute#{number}#{state}"

            @staticmethod
            def mutes(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#mute#{start}-{end}#{state}"

        class output:
            @staticmethod
            def gain(number: int, value: float):
                value = round(value, 2)
                return f"set:output#gain#{number}#{value}"

            @staticmethod
            def gains(start: int, end: int, value: float):
                value = round(value, 2)
                return f"set:output#gain#{start}-{end}#{value}"

            @staticmethod
            def mute(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#mute#{number}#{state}"

            @staticmethod
            def mutes(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#mute#{start}-{end}#{state}"


# Example usage
print(ASCII.get.input.gain(3))  # Output: get:input#gain#3
print(ASCII.get.input.gains(0, 7))  # Output: get:input#gain#0-7
print(ASCII.set.input.gain(3, -20.5))  # Output: set:input#gain#3#-20.5
print(ASCII.set.input.gains(0, 7, -20.5))  # Output: set:input#gain#0-7#-20.5

print(ASCII.get.input.phantom(1))  # Output: get:input#phant#1
print(ASCII.get.input.phantoms(0, 7))  # Output: get:input#phant#0-7
print(ASCII.set.input.phantom(1, 1))  # Output: set:input#phant#1#1
print(ASCII.set.input.phantoms(0, 7, 0))  # Output: set:input#phant#0-7#0
