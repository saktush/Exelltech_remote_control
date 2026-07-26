import socket
import unittest
from unittest.mock import patch, MagicMock
from modules.system import UDP
import ipaddress as ip


class TestUDP(unittest.TestCase):

    def setUp(self):
        self.local_ip = ip.ip_address("192.168.3.100")
        self.local_port = 50000
        self.dest_ip = ip.ip_address("192.168.3.110")
        self.dest_port = 50000
        self.speed = 0.01
        self.message = "Hello, World!"

    @patch('socket.socket')
    def test_send_success(self, mock_socket):
        # Create a mock socket object
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance

        # Mock the recv method to return a specific response
        mock_sock_instance.recv.return_value = self.message.encode("ascii")

        response = UDP.send(self.local_ip, self.local_port, self.dest_ip, self.dest_port, self.message)

        self.assertEqual(response, self.message)

        # Verify that the mock socket was used correctly
        mock_socket.return_value.__enter__.assert_called_once()
        mock_sock_instance.sendto.assert_called_with(self.message.encode("ascii"), (str(self.dest_ip), self.dest_port))
        mock_sock_instance.recv.assert_called_once_with(UDP.BUFFERSIZE)

    @patch('socket.socket')
    def test_send_timeout(self, mock_socket):
        # Create a mock socket object
        mock_sock_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_sock_instance

        # Mock the recv method to raise a timeout exception
        mock_sock_instance.recv.side_effect = socket.timeout

        response = UDP.send(self.local_ip, self.local_port, self.dest_ip, self.dest_port, self.message)

        self.assertIsNone(response)

        # Verify that the mock socket was used correctly
        mock_socket.return_value.__enter__.assert_called_once()
        mock_sock_instance.sendto.assert_called_with(self.message.encode("ascii"), (str(self.dest_ip), self.dest_port))
        mock_sock_instance.recv.assert_called_once_with(UDP.BUFFERSIZE)

    @patch('socket.socket')
    def test_send_invalid_ip(self, mock_socket):
        with self.assertRaises(ValueError):
            UDP.send("invalid_ip", self.local_port, self.dest_ip, self.dest_port, self.message)

        with self.assertRaises(ValueError):
            UDP.send(self.local_ip, self.local_port, "invalid_ip", self.dest_port, self.message)


if __name__ == '__main__':
    unittest.main()

