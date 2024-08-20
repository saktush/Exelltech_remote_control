import unittest
from unittest.mock import patch, MagicMock
from modules.system import UDP
from modules.abstract import Processor
from modules.driver import Driver
from config import LOCAL_IP, LOCAL_PORT


class TestChannelManager(unittest.TestCase):

    def setUp(self):
        # Create a mock Processor object
        self.proc = MagicMock(spec=Processor)
        self.proc.ip_addr = '192.168.3.10'
        self.proc.port = 5000
        self.proc.input_channels = [0, 1, 2]

        # Expected configuration values
        self.expected_local_ip = LOCAL_IP
        self.expected_local_port = LOCAL_PORT

    @patch('modules.api.ASCII.get.input.gains', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#1.0#2.0#3.0")
    def test_pull_input_channels_gain(self, mock_udp_send, mock_get_input_gains):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_input_channels_gain(self.proc)

        self.assertEqual(result, [1.0, 2.0, 3.0])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.output.gains', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#4.0#5.0#6.0")
    def test_pull_output_channels_gain(self, mock_udp_send, mock_get_output_gains):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_output_channels_gain(self.proc)

        self.assertEqual(result, [4.0, 5.0, 6.0])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.input.mutes', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#1#0#1")
    def test_pull_input_channels_mute(self, mock_udp_send, mock_get_input_mutes):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_input_channels_mute(self.proc)

        self.assertEqual(result, [True, False, True])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.output.mutes', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#0#0#1")
    def test_pull_output_channels_mute(self, mock_udp_send, mock_get_output_mutes):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_output_channels_mute(self.proc)

        self.assertEqual(result, [False, False, True])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.input.levels', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#10.0#20.0#30.0")
    def test_pull_input_channels_level(self, mock_udp_send, mock_get_input_levels):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_input_channels_level(self.proc)

        self.assertEqual(result, [10.0, 20.0, 30.0])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.output.levels', return_value="mock_command")
    @patch('modules.system.UDP.send', return_value="mock_command#15.0#25.0#35.0")
    def test_pull_output_channels_level(self, mock_udp_send, mock_get_output_levels):
        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.pull_output_channels_level(self.proc)

        self.assertEqual(result, [15.0, 25.0, 35.0])
        mock_udp_send.assert_called_with(self.expected_local_ip, self.expected_local_port, self.proc.ip_addr,
                                         self.proc.port, "mock_command")

    @patch('modules.api.ASCII.get.mixer.switch')
    @patch('modules.system.UDP.send')
    def test_pull_matrix_switches(self, mock_udp_send, mock_get_mixer_switch):
        self.proc.matrix = MagicMock()
        self.proc.matrix.routes = [[False, False, False], [False, False, False]]

        expected_responses = ["1", "0", "1", "1", "0", "0"]
        mock_udp_send.side_effect = expected_responses  # Simulate sequential calls

        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            Driver.pull_matrix_switches(self.proc)

        # Assert the expected interactions with the mock matrix routes
        expected_calls = [
            ((0, 0, True),), ((0, 1, False),), ((0, 2, True),),
            ((1, 0, True),), ((1, 1, False),), ((1, 2, False),)
        ]
        self.proc.matrix.set_route.assert_has_calls(expected_calls, any_order=True)

    @patch('modules.api.ASCII.set.mixer.switch')
    @patch('modules.system.UDP.send', return_value="success")
    def test_push_matrix_switches(self, mock_udp_send, mock_set_mixer_switch):
        self.proc.matrix = MagicMock()
        self.proc.matrix.routes = [[True, False, True], [False, True, False]]

        with patch('config.LOCAL_IP', new=self.expected_local_ip), patch('config.LOCAL_PORT',
                                                                         new=self.expected_local_port):
            result = Driver.push_matrix_switches(self.proc)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
