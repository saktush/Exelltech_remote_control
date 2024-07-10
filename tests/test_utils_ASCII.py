from models._utils import ASCII
import unittest


class TestASCIIMethods(unittest.TestCase):
    def test_get_input_gain(self):
        self.assertEqual(ASCII.get.input.gain(1), "get:input#gain#1")
        self.assertEqual(ASCII.get.input.gains(0, 7), "get:input#gain#0-7")

    def test_get_input_phantom(self):
        self.assertEqual(ASCII.get.input.phantom(1), "get:input#phant#1")
        self.assertEqual(ASCII.get.input.phantoms(0, 7), "get:input#phant#0-7")

    def test_get_input_mute(self):
        self.assertEqual(ASCII.get.input.mute(1), "get:input#mute#1")
        self.assertEqual(ASCII.get.input.mutes(0, 7), "get:input#mute#0-7")

    def test_get_input_sensitivity(self):
        self.assertEqual(ASCII.get.input.sensitivity(1), "get:input#sens#1")
        self.assertEqual(ASCII.get.input.sensitivities(0, 7), "get:input#sens#0-7")

    def test_get_input_phase(self):
        self.assertEqual(ASCII.get.input.phase(1), "get:input#phase#1")
        self.assertEqual(ASCII.get.input.phases(0, 7), "get:input#phase#0-7")

    def test_get_input_link(self):
        self.assertEqual(ASCII.get.input.link(1), "get:input#link#1")
        self.assertEqual(ASCII.get.input.links(0, 7), "get:input#link#0-7")

    def test_get_input_type(self):
        self.assertEqual(ASCII.get.input.type(1), "get:input#type#1")
        self.assertEqual(ASCII.get.input.types(0, 7), "get:input#type#0-7")

    def test_get_input_level(self):
        self.assertEqual(ASCII.get.input.level(1), "get:input#level#1")
        self.assertEqual(ASCII.get.input.levels(0, 7), "get:input#level#0-7")

    def test_get_output_gain(self):
        self.assertEqual(ASCII.get.output.gain(1), "get:output#gain#1")
        self.assertEqual(ASCII.get.output.gains(0, 7), "get:output#gain#0-7")

    def test_get_output_mute(self):
        self.assertEqual(ASCII.get.output.mute(1), "get:output#mute#1")
        self.assertEqual(ASCII.get.output.mutes(0, 7), "get:output#mute#0-7")

    def test_get_output_phase(self):
        self.assertEqual(ASCII.get.output.phase(1), "get:output#phase#1")
        self.assertEqual(ASCII.get.output.phases(0, 7), "get:output#phase#0-7")

    def test_get_output_link(self):
        self.assertEqual(ASCII.get.output.link(1), "get:output#link#1")
        self.assertEqual(ASCII.get.output.links(0, 7), "get:output#link#0-7")

    def test_get_output_level(self):
        self.assertEqual(ASCII.get.output.level(1), "get:output#level#1")
        self.assertEqual(ASCII.get.output.levels(0, 7), "get:output#level#0-7")

    def test_set_input_gain(self):
        self.assertEqual(ASCII.set.input.gain(1, 2.5), "set:input#gain#1#2.5")
        self.assertEqual(ASCII.set.input.gains(0, 7, 2.5), "set:input#gain#0-7#2.5")

    def test_set_input_phantom(self):
        self.assertEqual(ASCII.set.input.phantom(1, 1), "set:input#phant#1#1")
        self.assertEqual(ASCII.set.input.phantoms(0, 7, 0), "set:input#phant#0-7#0")

    def test_set_input_mute(self):
        self.assertEqual(ASCII.set.input.mute(1, 1), "set:input#mute#1#1")
        self.assertEqual(ASCII.set.input.mutes(0, 7, 0), "set:input#mute#0-7#0")

    def test_set_input_sensitivity(self):
        self.assertEqual(ASCII.set.input.sensitivity(1, 5), "set:input#sens#1#5")
        self.assertEqual(ASCII.set.input.sensitivities(0, 7, 5), "set:input#sens#0-7#5")

    def test_set_input_phase(self):
        self.assertEqual(ASCII.set.input.phase(1, 1), "set:input#phase#1#1")
        self.assertEqual(ASCII.set.input.phases(0, 7, 0), "set:input#phase#0-7#0")

    def test_set_input_link(self):
        self.assertEqual(ASCII.set.input.link(1, 1), "set:input#link#1#1")
        self.assertEqual(ASCII.set.input.links(0, 7, 0), "set:input#link#0-7#0")

    def test_set_input_type(self):
        self.assertEqual(ASCII.set.input.type(1, 1), "set:input#type#1#1")
        self.assertEqual(ASCII.set.input.types(0, 7, 0), "set:input#type#0-7#0")

    def test_set_output_gain(self):
        self.assertEqual(ASCII.set.output.gain(1, 2.5), "set:output#gain#1#2.5")
        self.assertEqual(ASCII.set.output.gains(0, 7, 2.5), "set:output#gain#0-7#2.5")

    def test_set_output_mute(self):
        self.assertEqual(ASCII.set.output.mute(1, 1), "set:output#mute#1#1")
        self.assertEqual(ASCII.set.output.mutes(0, 7, 0), "set:output#mute#0-7#0")

    def test_set_output_phase(self):
        self.assertEqual(ASCII.set.output.phase(1, 1), "set:output#phase#1#1")
        self.assertEqual(ASCII.set.output.phases(0, 7, 0), "set:output#phase#0-7#0")

    def test_set_output_link(self):
        self.assertEqual(ASCII.set.output.link(1, 1), "set:output#link#1#1")
        self.assertEqual(ASCII.set.output.links(0, 7, 0), "set:output#link#0-7#0")

    def test_get_mixer_switch(self):
        self.assertEqual(ASCII.get.mixer.switch(1, 2), "get:mixer#switch#1#2")
        self.assertEqual(ASCII.get.mixer.switch_vertical(1, (0, 3)), "get:mixer#switch#1#0-3")
        with self.assertRaises(ValueError):
            ASCII.get.mixer.switch_vertical(1, (3, 3))
        with self.assertRaises(ValueError):
            ASCII.get.mixer.switch_vertical(1, (4, 3))
        self.assertEqual(ASCII.get.mixer.switch_horizontal((0, 2), 3), "get:mixer#switch#0-2#3")
        with self.assertRaises(ValueError):
            ASCII.get.mixer.switch_horizontal((2, 2), 3)
        with self.assertRaises(ValueError):
            ASCII.get.mixer.switch_horizontal((2, 1), 3)

    def test_get_mixer_gain(self):
        self.assertEqual(ASCII.get.mixer.gain(1, 2), "get:mixer#gain#1#2")
        self.assertEqual(ASCII.get.mixer.gain_vertical(1, (0, 3)), "get:mixer#gain#1#0-3")
        with self.assertRaises(ValueError):
            ASCII.get.mixer.gain_vertical(1, (3, 3))
        with self.assertRaises(ValueError):
            ASCII.get.mixer.gain_vertical(1, (4, 3))
        self.assertEqual(ASCII.get.mixer.gain_horizontal((0, 2), 3), "get:mixer#gain#0-2#3")
        with self.assertRaises(ValueError):
            ASCII.get.mixer.gain_horizontal((2, 2), 3)
        with self.assertRaises(ValueError):
            ASCII.get.mixer.gain_horizontal((2, 1), 3)

    def test_set_mixer_switch(self):
        self.assertEqual(ASCII.set.mixer.switch(1, 2, 1), "set:mixer#switch#1#2#1")
        with self.assertRaises(ValueError):
            ASCII.set.mixer.switch(1, 2, 2)
        self.assertEqual(ASCII.set.mixer.switch_vertical(1, (0, 3), 1), "set:mixer#switch#1#0-3#1")
        with self.assertRaises(ValueError):
            ASCII.set.mixer.switch_vertical(1, (3, 3), 1)
        with self.assertRaises(ValueError):
            ASCII.set.mixer.switch_vertical(1, (0, 3), 2)
        self.assertEqual(ASCII.set.mixer.switch_horizontal((0, 2), 3, 1), "set:mixer#switch#0-2#3#1")
        with self.assertRaises(ValueError):
            ASCII.set.mixer.switch_horizontal((2, 2), 3, 1)
        with self.assertRaises(ValueError):
            ASCII.set.mixer.switch_horizontal((0, 2), 3, 2)

    def test_set_mixer_gain(self):
        self.assertEqual(ASCII.set.mixer.gain(1, 2, -20.5), "set:mixer#gain#1#2#-20.5")
        self.assertEqual(ASCII.set.mixer.gain_vertical(1, (0, 3), -20.5), "set:mixer#gain#1#0-3#-20.5")
        with self.assertRaises(ValueError):
            ASCII.set.mixer.gain_vertical(1, (3, 3), -20.5)
        self.assertEqual(ASCII.set.mixer.gain_horizontal((0, 2), 3, -20.5), "set:mixer#gain#0-2#3#-20.5")
        with self.assertRaises(ValueError):
            ASCII.set.mixer.gain_horizontal((2, 2), 3, -20.5)
        with self.assertRaises(ValueError):
            ASCII.set.mixer.gain_horizontal((2, 1), 3, -20.5)


if __name__ == "__main__":
    unittest.main()