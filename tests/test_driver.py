import unittest
from unittest.mock import MagicMock, patch

from exelltech_remote_control.abstract import Processor
from exelltech_remote_control.driver import Driver
from exelltech_remote_control.exceptions import CommunicationError


class TestDriver(unittest.TestCase):
    def setUp(self):
        # Create a mock Processor object with asymmetric input/output channel
        # counts, so that any code accidentally using the input count for
        # output-channel commands is caught rather than masked.
        self.proc = MagicMock(spec=Processor)
        self.proc.ip_addr = "192.168.1.20"
        self.proc.port = 5000
        self.proc.local_ip = "192.168.1.10"
        self.proc.local_port = 50000
        self.proc.input_channels = [0, 1, 2]
        self.proc.output_channels = [0, 1, 2, 3, 4]

    @patch("exelltech_remote_control.api.ASCII.get.input.gains", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#1.0#2.0#3.0")
    def test_pull_input_channels_gain(self, mock_udp_send, mock_get_input_gains):
        result = Driver.pull_input_channels_gain(self.proc)

        mock_get_input_gains.assert_called_once_with(0, len(self.proc.input_channels))
        self.assertEqual(result, [1.0, 2.0, 3.0])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.output.gains", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#4.0#5.0#6.0#7.0#8.0")
    def test_pull_output_channels_gain(self, mock_udp_send, mock_get_output_gains):
        result = Driver.pull_output_channels_gain(self.proc)

        # Regression: this used to build its range from len(input_channels).
        mock_get_output_gains.assert_called_once_with(0, len(self.proc.output_channels))
        self.assertEqual(result, [4.0, 5.0, 6.0, 7.0, 8.0])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.input.mutes", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#1#0#1")
    def test_pull_input_channels_mute(self, mock_udp_send, mock_get_input_mutes):
        result = Driver.pull_input_channels_mute(self.proc)

        mock_get_input_mutes.assert_called_once_with(0, len(self.proc.input_channels))
        self.assertEqual(result, [True, False, True])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.output.mutes", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#0#0#1#1#0")
    def test_pull_output_channels_mute(self, mock_udp_send, mock_get_output_mutes):
        result = Driver.pull_output_channels_mute(self.proc)

        # Regression: this used to build its range from len(input_channels).
        mock_get_output_mutes.assert_called_once_with(0, len(self.proc.output_channels))
        self.assertEqual(result, [False, False, True, True, False])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.input.levels", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#10.0#20.0#30.0")
    def test_pull_input_channels_level(self, mock_udp_send, mock_get_input_levels):
        result = Driver.pull_input_channels_level(self.proc)

        mock_get_input_levels.assert_called_once_with(0, len(self.proc.input_channels))
        self.assertEqual(result, [10.0, 20.0, 30.0])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.output.levels", return_value="mock_command")
    @patch("exelltech_remote_control.system.UDP.send", return_value="mock_command#15.0#25.0#35.0#45.0#55.0")
    def test_pull_output_channels_level(self, mock_udp_send, mock_get_output_levels):
        result = Driver.pull_output_channels_level(self.proc)

        # Regression: this used to build its range from len(input_channels).
        mock_get_output_levels.assert_called_once_with(0, len(self.proc.output_channels))
        self.assertEqual(result, [15.0, 25.0, 35.0, 45.0, 55.0])
        mock_udp_send.assert_called_with(
            self.proc.local_ip, self.proc.local_port, self.proc.ip_addr, self.proc.port, "mock_command"
        )

    @patch("exelltech_remote_control.api.ASCII.get.mixer.switch_vertical")
    @patch("exelltech_remote_control.system.UDP.send")
    def test_pull_matrix_switches_batches_by_row(self, mock_udp_send, mock_switch_vertical):
        self.proc.matrix = MagicMock()
        self.proc.matrix.inputs = 2
        self.proc.matrix.outputs = 3

        mock_switch_vertical.side_effect = lambda row, col_range: f"cmd_row{row}_{col_range[0]}-{col_range[1]}"
        mock_udp_send.side_effect = [
            "cmd_row0_0-3#1#0#1",
            "cmd_row1_0-3#0#1#0",
        ]

        Driver.pull_matrix_switches(self.proc)

        # Regression: this used to issue one UDP call per cell (inputs * outputs)
        # instead of one call per row.
        self.assertEqual(mock_udp_send.call_count, 2)
        expected_calls = [
            ((0, 0, True),),
            ((0, 1, False),),
            ((0, 2, True),),
            ((1, 0, False),),
            ((1, 1, True),),
            ((1, 2, False),),
        ]
        self.proc.matrix.set_route.assert_has_calls(expected_calls, any_order=True)

    @patch("exelltech_remote_control.api.ASCII.set.mixer.switch")
    @patch("exelltech_remote_control.system.UDP.send", return_value="success")
    def test_push_matrix_switches_writes_every_cell(self, mock_udp_send, mock_set_mixer_switch):
        self.proc.matrix = MagicMock()
        self.proc.matrix.routes = [[True, False, True], [False, True, False]]

        result = Driver.push_matrix_switches(self.proc)

        self.assertTrue(result)
        # Regression: this used to return after writing only the first cell.
        self.assertEqual(mock_udp_send.call_count, 6)

    @patch("exelltech_remote_control.api.ASCII.set.mixer.switch")
    @patch("exelltech_remote_control.system.UDP.send")
    def test_push_matrix_switches_reports_failure_without_stopping_early(self, mock_udp_send, mock_set_mixer_switch):
        self.proc.matrix = MagicMock()
        self.proc.matrix.routes = [[True, False, True], [False, True, False]]
        mock_udp_send.side_effect = [None, "ok", "ok", "ok", "ok", "ok"]

        result = Driver.push_matrix_switches(self.proc)

        self.assertFalse(result)
        self.assertEqual(mock_udp_send.call_count, 6)

    @patch("exelltech_remote_control.system.UDP.send", side_effect=RuntimeError("socket failed"))
    def test_get_ascii_raises_communication_error_on_transport_failure(self, mock_udp_send):
        with self.assertRaises(CommunicationError) as ctx:
            Driver._get_ascii(self.proc, "get:input#gain#0")

        self.assertIsInstance(ctx.exception.__cause__, RuntimeError)


if __name__ == "__main__":
    unittest.main()
