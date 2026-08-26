import ipaddress
import unittest
from unittest.mock import patch

from exelltech_remote_control.channel import InputChannel, OutputChannel
from exelltech_remote_control.driver import Driver
from exelltech_remote_control.matrix import Matrix
from exelltech_remote_control.processor import ELTProcessor


class TestELTProcessor(unittest.TestCase):
    def setUp(self):
        self.ip_addr = ipaddress.ip_address("192.168.1.1")
        self.port = 8080
        self.inputs = 4
        self.outputs = 4
        self.processor = ELTProcessor(self.ip_addr, self.port, self.inputs, self.outputs, 2)

    def test_initialization(self):
        self.assertEqual(self.processor.ip_addr, self.ip_addr)
        self.assertEqual(self.processor.port, self.port)
        self.assertFalse(self.processor.system_mute)
        self.assertEqual(len(self.processor.scenes), 16)
        self.assertEqual(len(self.processor.input_channels), self.inputs)
        self.assertEqual(len(self.processor.output_channels), self.outputs)
        self.assertIsInstance(self.processor.matrix, Matrix)

    def test_ip_addr_setter(self):
        new_ip = "192.168.1.2"
        self.processor.ip_addr = new_ip
        self.assertEqual(self.processor.ip_addr, ipaddress.ip_address(new_ip))

        with self.assertRaises(ValueError):
            self.processor.ip_addr = "invalid_ip"

    def test_port_setter(self):
        new_port = 9090
        self.processor.port = new_port
        self.assertEqual(self.processor.port, new_port)

    def test_local_ip_and_port_defaults(self):
        self.assertEqual(self.processor.local_ip, ipaddress.ip_address("0.0.0.0"))
        self.assertEqual(self.processor.local_port, 50000)

    def test_local_ip_and_port_constructor_args(self):
        processor = ELTProcessor(
            self.ip_addr, self.port, self.inputs, self.outputs, 2, local_ip="192.168.1.50", local_port=50001
        )
        self.assertEqual(processor.local_ip, ipaddress.ip_address("192.168.1.50"))
        self.assertEqual(processor.local_port, 50001)

    def test_system_mute_setter(self):
        self.processor.system_mute = True
        self.assertTrue(self.processor.system_mute)
        self.processor.system_mute = False
        self.assertFalse(self.processor.system_mute)

    def test_input_channels(self):
        self.assertIsInstance(self.processor.input_channels[0], InputChannel)

    def test_output_channels(self):
        self.assertIsInstance(self.processor.output_channels[0], OutputChannel)

    def test_matrix(self):
        self.assertIsInstance(self.processor.matrix, Matrix)
        self.assertEqual(self.processor.matrix.inputs, self.inputs)
        self.assertEqual(self.processor.matrix.outputs, self.outputs)

    def test_repr_is_implemented(self):
        text = repr(self.processor)
        self.assertIn("ELTProcessor", text)
        self.assertIn(str(self.processor.ip_addr), text)

    @patch.object(Driver, "pull_matrix_switches")
    def test_pull_matrix_delegates_to_driver(self, mock_pull):
        self.processor.pull_matrix()
        mock_pull.assert_called_once_with(self.processor)

    @patch.object(Driver, "push_matrix_switches", return_value=True)
    def test_push_matrix_delegates_to_driver(self, mock_push):
        result = self.processor.push_matrix()
        self.assertTrue(result)
        mock_push.assert_called_once_with(self.processor)


class TestELTProcessorPullChannels(unittest.TestCase):
    """Regression coverage for the pull_channels() output-channel mute/level bugs."""

    def setUp(self):
        self.processor = ELTProcessor("192.168.1.1", 8080, 2, 2, None)

    @patch.object(Driver, "pull_output_channels_level", return_value=[-10.0, -20.0])
    @patch.object(Driver, "pull_input_channels_level", return_value=[-30.0, -40.0])
    @patch.object(Driver, "pull_output_channels_mute", return_value=[True, True])
    @patch.object(Driver, "pull_input_channels_mute", return_value=[False, False])
    @patch.object(Driver, "pull_output_channels_gain", return_value=[1.0, 2.0])
    @patch.object(Driver, "pull_input_channels_gain", return_value=[3.0, 4.0])
    def test_pull_channels_sets_output_mute_correctly(self, *_mocks):
        self.processor.pull_channels()

        for o_ch in self.processor.output_channels:
            self.assertTrue(o_ch.mute)
            self.assertFalse(hasattr(o_ch, "mutes"))

    @patch.object(Driver, "pull_output_channels_level", return_value=[-10.0, -20.0])
    @patch.object(Driver, "pull_input_channels_level", return_value=[-30.0, -40.0])
    @patch.object(Driver, "pull_output_channels_mute", return_value=[True, True])
    @patch.object(Driver, "pull_input_channels_mute", return_value=[False, False])
    @patch.object(Driver, "pull_output_channels_gain", return_value=[1.0, 2.0])
    @patch.object(Driver, "pull_input_channels_gain", return_value=[3.0, 4.0])
    def test_pull_channels_sets_output_level_from_output_data(self, *_mocks):
        self.processor.pull_channels()

        self.assertEqual([ch.level for ch in self.processor.output_channels], [-10.0, -20.0])
        self.assertEqual([ch.level for ch in self.processor.input_channels], [-30.0, -40.0])


class TestELTProcessorAsymmetric(unittest.TestCase):
    """Regression coverage for asymmetric input/output channel counts."""

    def setUp(self):
        self.processor = ELTProcessor("192.168.1.1", 8080, 8, 4, None)

    def test_channel_counts_differ(self):
        self.assertEqual(len(self.processor.input_channels), 8)
        self.assertEqual(len(self.processor.output_channels), 4)

    @patch.object(Driver, "pull_output_channels_level", return_value=None)
    @patch.object(Driver, "pull_input_channels_level", return_value=None)
    @patch.object(Driver, "pull_output_channels_mute", return_value=None)
    @patch.object(Driver, "pull_input_channels_mute", return_value=None)
    @patch.object(Driver, "pull_output_channels_gain", return_value=[1.0, 2.0, 3.0, 4.0])
    @patch.object(Driver, "pull_input_channels_gain", return_value=[0.0] * 8)
    def test_pull_channels_maps_output_gain_by_output_index(self, *_mocks):
        self.processor.pull_channels()
        self.assertEqual([ch.gain for ch in self.processor.output_channels], [1.0, 2.0, 3.0, 4.0])


if __name__ == "__main__":
    unittest.main()
