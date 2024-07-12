import socket
import ipaddress as ip


def bytes_to_hex(b_string: bytes) -> str:
    return b_string.hex()


def bytes_to_ascii(b_string: bytes) -> str:
    return b_string.decode('ascii')


def str_to_bytes(message: str) -> bytes:
    return message.encode("ascii")


def hex_to_bytes(message: str) -> bytes:
    return bytes.fromhex(message)


class UDP:
    TIMEOUT: float = 0.25
    BUFFERSIZE: int = 256

    @staticmethod
    def send(source_ip: ip.IPv4Address, source_port: int, dest_ip: ip.IPv4Address, dest_port: int,
             message: str) -> str | None:
        try:
            message = str_to_bytes(message)
        except UnicodeEncodeError as e:
            raise e

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((source_ip, source_port))
            sock.settimeout(UDP.TIMEOUT)
            sock.sendto(message, (dest_ip, dest_port))
            try:
                response = sock.recv(UDP.BUFFERSIZE)
            except socket.timeout:
                response = None
            finally:
                sock.close()

        if response:
            return bytes_to_ascii(response)
