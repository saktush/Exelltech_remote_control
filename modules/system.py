import socket
import ipaddress as ip
from typing import Union


def bytes_to_hex(b_string: bytes) -> str:
    return b_string.hex()


def bytes_to_ascii(b_string: bytes) -> str:
    return b_string.decode('ascii')


def ascii_to_bytes(message: str) -> bytes:
    return message.encode("ascii")


def hex_to_bytes(message: str) -> bytes:
    return bytes.fromhex(message)


def ping_server(server: str, port: int, timeout=3):
    """ping server"""
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
    except OSError as error:
        return False
    else:
        s.close()
        return True


class UDP:
    """
    A class encapsulating UDP communication functionalities with configurable timeout and buffer size.
    Provides methods to send and receive UDP messages with proper handling of IP addresses
    and message encoding.

    - param TIMEOUT: float
    - param BUFFERSIZE: int

    """
    TIMEOUT: float = 0.25
    BUFFERSIZE: int = 256

    @staticmethod
    def send(source_ip: Union[ip.IPv4Address, str], source_port: int,
             dest_ip: Union[ip.IPv4Address, str], dest_port: int,
             message: str) -> Union[str, None]:
        """
        Sends a UDP message from the specified source to the destination. Handles conversion
        of message to bytes and automatically closes the socket after the operation.

        :param source_ip: IPv4Address | str: The source IPv4 address.
        :param source_port: int: The source port number.
        :param dest_ip: Pv4Address | str: The destination IPv4 address.
        :param dest_port: int: The destination port number.
        :param message: str: ASCII message to send

        :return: str | None: The response message decoded to ASCII, or None if there is a timeout.

        :raises ValueError: If IP addresses or port numbers are not valid.
        :raises UnicodeEncodeError: If message encoding fails.
        :raises RuntimeError: If a socket operation fails.
        """
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
            message_bytes = ascii_to_bytes(message)
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
