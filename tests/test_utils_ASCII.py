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

    def test_get_system_mute(self):
        self.assertEqual(ASCII.get.sysctl.mute(), "get:sysctl#mute")

    def test_set_system_mute(self):
        self.assertEqual(ASCII.set.sysctl.mute(1), "set:sysctl#mute#1")
        self.assertEqual(ASCII.set.sysctl.mute(0), "set:sysctl#mute#0")
        with self.assertRaises(ValueError):
            ASCII.set.sysctl.mute(2)
        with self.assertRaises(ValueError):
            ASCII.set.sysctl.mute(-1)

    def test_get_input_name(self):
        self.assertEqual(ASCII.get.input.name(1), "get:input#name#1")
        self.assertEqual(ASCII.get.input.names(0, 7), "get:input#name#0-7")
        with self.assertRaises(ValueError):
            ASCII.get.input.names(7, 7)
        with self.assertRaises(ValueError):
            ASCII.get.input.names(8, 7)

    def test_get_output_name(self):
        self.assertEqual(ASCII.get.output.name(1), "get:output#name#1")
        self.assertEqual(ASCII.get.output.names(0, 7), "get:output#name#0-7")
        with self.assertRaises(ValueError):
            ASCII.get.output.names(7, 7)
        with self.assertRaises(ValueError):
            ASCII.get.output.names(8, 7)

    def test_set_input_name(self):
        self.assertEqual(ASCII.set.input.name(0, "Hello"), "set:input#name#0#Hello")
        with self.assertRaises(ValueError):
            ASCII.set.input.name(0, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.input.name(0, "HelloWorld😊")

        self.assertEqual(ASCII.set.input.names(0, 1, "Hello"), "set:input#name#0-1#Hello")
        with self.assertRaises(ValueError):
            ASCII.set.input.names(0, 1, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.input.names(0, 1, "HelloWorld😊")
        with self.assertRaises(ValueError):
            ASCII.set.input.names(1, 1, "Hello")
        with self.assertRaises(ValueError):
            ASCII.set.input.names(2, 1, "Hello")

    def test_set_output_name(self):
        self.assertEqual(ASCII.set.output.name(0, "World"), "set:output#name#0#World")
        with self.assertRaises(ValueError):
            ASCII.set.output.name(0, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.output.name(0, "HelloWorld😊")

        self.assertEqual(ASCII.set.output.names(0, 1, "World"), "set:output#name#0-1#World")
        with self.assertRaises(ValueError):
            ASCII.set.output.names(0, 1, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.output.names(0, 1, "HelloWorld😊")
        with self.assertRaises(ValueError):
            ASCII.set.output.names(1, 1, "World")
        with self.assertRaises(ValueError):
            ASCII.set.output.names(2, 1, "World")

    def test_get_scene_name(self):
        self.assertEqual(ASCII.get.scene.name(1), "get:scene#name#1")
        self.assertEqual(ASCII.get.scene.names(0, 15), "get:scene#name#0-15")
        with self.assertRaises(ValueError):
            ASCII.get.scene.names(15, 15)
        with self.assertRaises(ValueError):
            ASCII.get.scene.names(16, 15)

    def test_set_scene_name(self):
        self.assertEqual(ASCII.set.scene.name(0, "Hello"), "set:scene#name#0#Hello")
        with self.assertRaises(ValueError):
            ASCII.set.scene.name(0, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.scene.name(0, "HelloWorld😊")

        self.assertEqual(ASCII.set.scene.names(0, 1, "Hello"), "set:scene#name#0-1#Hello")
        with self.assertRaises(ValueError):
            ASCII.set.scene.names(0, 1, "HelloWorld123456")
        with self.assertRaises(ValueError):
            ASCII.set.scene.names(0, 1, "HelloWorld😊")
        with self.assertRaises(ValueError):
            ASCII.set.scene.names(1, 1, "Hello")
        with self.assertRaises(ValueError):
            ASCII.set.scene.names(2, 1, "Hello")

    def test_scene_save(self):
        self.assertEqual(ASCII.scene.save(1), "scene:save#1")
        with self.assertRaises(ValueError):
            ASCII.scene.save(16)
        with self.assertRaises(ValueError):
            ASCII.scene.save(-1)

    def test_scene_toggle(self):
        self.assertEqual(ASCII.scene.toggle(1), "scene:toggle#1")
        with self.assertRaises(ValueError):
            ASCII.scene.toggle(16)
        with self.assertRaises(ValueError):
            ASCII.scene.toggle(-1)


if __name__ == "__main__":
    unittest.main()
