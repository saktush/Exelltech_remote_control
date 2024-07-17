import unittest
import ipaddress
from models.channel import InputChannel, OutputChannel
from models.matrix import Matrix
from models.processor import ELTProcessor


class TestELTProcessor(unittest.TestCase):

    def setUp(self):
        self.ip_addr = ipaddress.ip_address('192.168.1.1')
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
        new_ip = '192.168.1.2'
        self.processor.ip_addr = new_ip
        self.assertEqual(self.processor.ip_addr, ipaddress.ip_address(new_ip))

        with self.assertRaises(ValueError):
            self.processor.ip_addr = 'invalid_ip'

    def test_port_setter(self):
        new_port = 9090
        self.processor.port = new_port
        self.assertEqual(self.processor.port, new_port)

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


if __name__ == "__main__":
    unittest.main()
