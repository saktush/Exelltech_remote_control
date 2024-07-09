import unittest
from models.channel import Channel, InputChannel, OutputChannel


class TestChannel(unittest.TestCase):

    def setUp(self):
        self.channel = Channel()

    def test_channel_init(self):
        self.assertEqual(self.channel.number, 0)
        self.assertEqual(self.channel.name, '')
        self.assertFalse(self.channel.mute)
        self.assertFalse(self.channel.link)
        self.assertEqual(self.channel.gain, 0.0)
        self.assertEqual(self.channel.level, -160.0)

    def test_channel_setter(self):
        self.channel.name = 'Test Channel'
        self.assertEqual(self.channel.name, 'Test Channel')
        self.channel.mute = True
        self.assertTrue(self.channel.mute)
        self.channel.link = True
        self.assertTrue(self.channel.link)

    def test_channel_str(self):
        # self.channel.number = 1
        self.channel.name = 'My Channel'
        self.channel.mute = False
        self.channel.gain = 6.0
        self.channel.link = False
        # self.channel.level = -120.0
        expected_string = (f"Channel 0: My Channel - Mute: "
                           f"{self.channel.mute}, Gain: {self.channel.gain}, "
                           f"Linked: {self.channel.link}, Level: {self.channel.level}")
        self.assertEqual(str(self.channel), expected_string)


class TestInputChannel(unittest.TestCase):

    def setUp(self):
        self.input_channel = InputChannel(1, is_dante=False)

    def test_input_channel_init(self):
        self.assertEqual(self.input_channel.number, 1)
        self.assertEqual(self.input_channel.name, 'IN2')
        self.assertFalse(self.input_channel.mute)
        self.assertFalse(self.input_channel.link)
        self.assertEqual(self.input_channel.gain, 0.0)
        self.assertEqual(self.input_channel.level, -160.0)

    def test_input_channel_setter(self):
        self.input_channel.source = 'generator'
        self.assertEqual(self.input_channel.source, 'generator')
        with self.assertRaises(ValueError):
            self.input_channel.sensitivity = 20
        with self.assertRaises(ValueError):
            self.input_channel.phantom_power = None


class TestOutputChannel(unittest.TestCase):

    def setUp(self):
        self.output_channel = OutputChannel(1, is_dante=False)

    def test_output_channel_init(self):
        self.assertEqual(self.output_channel.number, 1)
        self.assertEqual(self.output_channel.name, 'OUT2')
        self.assertFalse(self.output_channel.mute)
        self.assertFalse(self.output_channel.link)
        self.assertEqual(self.output_channel.gain, 0.0)
        self.assertEqual(self.output_channel.level, -160.0)

    def test_output_channel_setter(self):
        self.output_channel.phase = True
        self.assertTrue(self.output_channel.phase)


if __name__ == '__main__':
    unittest.main()
