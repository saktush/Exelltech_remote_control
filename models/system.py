import socket
import ipaddress as ip
from typing import Union


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
    def send(source_ip: Union[ip.IPv4Address, str], source_port: int,
             dest_ip: Union[ip.IPv4Address, str], dest_port: int,
             message: str) -> Union[str, None]:

        if not isinstance(source_ip, (str, ip.IPv4Address)) or not isinstance(dest_ip, (str, ip.IPv4Address)):
            raise ValueError("IP addresses should be of type str or ip.IPv4Address")

        source_ip = str(source_ip) if isinstance(source_ip, ip.IPv4Address) else source_ip
        dest_ip = str(dest_ip) if isinstance(dest_ip, ip.IPv4Address) else dest_ip

        try:
            ip.ip_address(source_ip)
            ip.ip_address(dest_ip)
        except ValueError as e:
            raise ValueError(f"Invalid IP address: {e}")

        if not isinstance(source_port, int) or not isinstance(dest_port, int):
            raise ValueError("Ports should be integers")

        try:
            message_bytes = str_to_bytes(message)
        except UnicodeEncodeError as e:
            raise ValueError(f"Message encoding failed: {e}")

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            try:
                sock.bind((source_ip, source_port))
                sock.settimeout(UDP.TIMEOUT)
                sock.sendto(message_bytes, (dest_ip, dest_port))
                try:
                    response = sock.recv(UDP.BUFFERSIZE)
                    return bytes_to_ascii(response)
                except socket.timeout:
                    return None
            except socket.error as e:
                raise RuntimeError(f"Socket operation failed: {e}")

        return None
