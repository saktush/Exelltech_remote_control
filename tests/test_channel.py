import unittest
from modules.channel import Channel, InputChannel, OutputChannel


class TestInputChannel(unittest.TestCase):

    def setUp(self):
        self.input_channel = InputChannel(number=0, is_digital=False)

    def test_initialization(self):
        self.assertEqual(self.input_channel.number, 0)
        self.assertEqual(self.input_channel.name, 'IN1')
        self.assertFalse(self.input_channel.mute)
        self.assertEqual(self.input_channel.gain, 0.0)
        self.assertFalse(self.input_channel.link)
        self.assertEqual(self.input_channel.level, -160.0)
        self.assertFalse(self.input_channel.is_digital)
        
    def test_name_setter(self):
        self.input_channel.name = "Test input_ch"
        self.assertEqual(self.input_channel.name, "Test input_ch")

        with self.assertRaises(ValueError):
            self.input_channel.name = 123  # Not a string

        with self.assertRaises(ValueError):
            self.input_channel.name = "A" * 17  # Length exceeds 16 chars

        with self.assertRaises(ValueError):
            self.input_channel.name = "Chånnel"  # Non-ASCII character

    def test_mute_setter(self):
        self.input_channel.mute = True
        self.assertTrue(self.input_channel.mute)

        with self.assertRaises(ValueError):
            self.input_channel.mute = "yes"  # Not a boolean

    def test_gain_setter(self):
        self.input_channel.gain = -70.0
        self.assertEqual(self.input_channel.gain, -70.0)

        with self.assertRaises(ValueError):
            self.input_channel.gain = -80.0  # Out of range

        with self.assertRaises(ValueError):
            self.input_channel.gain = 20.0  # Out of range

        with self.assertRaises(ValueError):
            self.input_channel.gain = "high"  # Not a float

    def test_link_setter(self):
        self.input_channel.link = True
        self.assertTrue(self.input_channel.link)

        with self.assertRaises(ValueError):
            self.input_channel.link = "connected"  # Not a boolean

    def test_source_setter(self):
        self.input_channel.source = "generator"
        self.assertEqual(self.input_channel.source, "generator")

        with self.assertRaises(ValueError):
            self.input_channel.source = "external"  # Invalid value

        with self.assertRaises(ValueError):
            self.input_channel.source = 5  # Not a string

    def test_sensitivity_property(self):
        self.input_channel.sensitivity = 5
        self.assertEqual(self.input_channel.sensitivity, 5)

        with self.assertRaises(ValueError):
            self.input_channel.sensitivity = 20  # Out of range

        with self.assertRaises(ValueError):
            self.input_channel.sensitivity = "high"  # Not an integer

    def test_phantom_power_property(self):
        self.input_channel.phantom_power = True
        self.assertTrue(self.input_channel.phantom_power)

        with self.assertRaises(ValueError):
            self.input_channel.phantom_power = "on"  # Not a boolean

    def test_phase_setter(self):
        self.input_channel.phase = True
        self.assertTrue(self.input_channel.phase)

        with self.assertRaises(ValueError):
            self.input_channel.phase = "reversed"  # Not a boolean

    def test_digital_channel_restrictions(self):
        digital_channel = InputChannel(number=1, is_digital=True)
        with self.assertRaises(AttributeError):
            digital_channel.sensitivity

        with self.assertRaises(AttributeError):
            digital_channel.phantom_power = True


class TestOutputChannel(unittest.TestCase):

    def setUp(self):
        self.output_channel = OutputChannel(number=1, is_digital=False)

    def test_initialization(self):
        self.assertEqual(self.output_channel.number, 1)
        self.assertEqual(self.output_channel.name, 'OUT2')
        self.assertFalse(self.output_channel.mute)
        self.assertEqual(self.output_channel.gain, 0.0)
        self.assertFalse(self.output_channel.link)
        self.assertEqual(self.output_channel.level, -160.0)
        self.assertFalse(self.output_channel.is_digital)

    def test_name_setter(self):
        self.output_channel.name = "Test output_ch"
        self.assertEqual(self.output_channel.name, "Test output_ch")

        with self.assertRaises(ValueError):
            self.output_channel.name = 123  # Not a string

        with self.assertRaises(ValueError):
            self.output_channel.name = "A" * 17  # Length exceeds 16 chars

        with self.assertRaises(ValueError):
            self.output_channel.name = "Chånnel"  # Non-ASCII character

    def test_mute_setter(self):
        self.output_channel.mute = True
        self.assertTrue(self.output_channel.mute)

        with self.assertRaises(ValueError):
            self.output_channel.mute = "yes"  # Not a boolean

    def test_gain_setter(self):
        self.output_channel.gain = -70.0
        self.assertEqual(self.output_channel.gain, -70.0)

        with self.assertRaises(ValueError):
            self.output_channel.gain = -80.0  # Out of range

        with self.assertRaises(ValueError):
            self.output_channel.gain = 20.0  # Out of range

        with self.assertRaises(ValueError):
            self.output_channel.gain = "high"  # Not a float

    def test_link_setter(self):
        self.output_channel.link = True
        self.assertTrue(self.output_channel.link)

        with self.assertRaises(ValueError):
            self.output_channel.link = "connected"  # Not a boolean

    def test_phase_setter(self):
        self.output_channel.phase = True
        self.assertTrue(self.output_channel.phase)

        with self.assertRaises(ValueError):
            self.output_channel.phase = "reversed"  # Not a boolean


if __name__ == '__main__':
    unittest.main()
