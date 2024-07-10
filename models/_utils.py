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

            @staticmethod
            def sensitivity(number: int):
                return f"get:input#sens#{number}"

            @staticmethod
            def sensitivities(start: int, end: int):
                return f"get:input#sens#{start}-{end}"

            @staticmethod
            def phase(number: int):
                return f"get:input#phase#{number}"

            @staticmethod
            def phases(start: int, end: int):
                return f"get:input#phase#{start}-{end}"

            @staticmethod
            def link(number: int):
                return f"get:input#link#{number}"

            @staticmethod
            def links(start: int, end: int):
                return f"get:input#link#{start}-{end}"

            @staticmethod
            def type(number: int):
                return f"get:input#type#{number}"

            @staticmethod
            def types(start: int, end: int):
                return f"get:input#type#{start}-{end}"

            @staticmethod
            def level(number: int):
                return f"get:input#level#{number}"

            @staticmethod
            def levels(start: int, end: int):
                return f"get:input#level#{start}-{end}"

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

            @staticmethod
            def phase(number: int):
                return f"get:output#phase#{number}"

            @staticmethod
            def phases(start: int, end: int):
                return f"get:output#phase#{start}-{end}"

            @staticmethod
            def link(number: int):
                return f"get:output#link#{number}"

            @staticmethod
            def links(start: int, end: int):
                return f"get:output#link#{start}-{end}"

            @staticmethod
            def level(number: int):
                return f"get:output#level#{number}"

            @staticmethod
            def levels(start: int, end: int):
                return f"get:output#level#{start}-{end}"

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

            @staticmethod
            def sensitivity(number: int, value: int):
                return f"set:input#sens#{number}#{value}"

            @staticmethod
            def sensitivities(start: int, end: int, value: int):
                return f"set:input#sens#{start}-{end}#{value}"

            @staticmethod
            def phase(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phase#{number}#{state}"

            @staticmethod
            def phases(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#phase#{start}-{end}#{state}"

            @staticmethod
            def link(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#link#{number}#{state}"

            @staticmethod
            def links(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:input#link#{start}-{end}#{state}"

            @staticmethod
            def type(number: int, value: int):
                if value not in (0, 1):
                    raise ValueError("Value must be 0 or 1")
                return f"set:input#type#{number}#{value}"

            @staticmethod
            def types(start: int, end: int, value: int):
                if value not in (0, 1):
                    raise ValueError("Value must be 0 or 1")
                return f"set:input#type#{start}-{end}#{value}"

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

            @staticmethod
            def phase(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#phase#{number}#{state}"

            @staticmethod
            def phases(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#phase#{start}-{end}#{state}"

            @staticmethod
            def link(number: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#link#{number}#{state}"

            @staticmethod
            def links(start: int, end: int, state: int):
                if state not in (0, 1):
                    raise ValueError("State must be 0 (off) or 1 (on)")
                return f"set:output#link#{start}-{end}#{state}"


