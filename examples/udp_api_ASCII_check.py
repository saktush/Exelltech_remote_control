import inspect
import unittest
import ipaddress as ip
from types import FunctionType
from typing import Type, List, Dict, Optional, Set
from models.api import ASCII
from models.system import UDP


def get_methods_from_class(cls: Type) -> List[str]:
    """
    Retrieve all method names from the given class.

    :param cls: The class object to retrieve methods from.
    :return: A list of method names.
    """
    methods = []
    for name, obj in inspect.getmembers(cls):
        if isinstance(obj, FunctionType):
            methods.append(name)
    return methods


def recursive_collect_methods(cls: Type, prefix: str = "", visited: Optional[Set[Type]] = None) -> Dict[str, List[str]]:
    """
    Recursively collect methods from the class and its nested classes.

    :param cls: The class object to start collecting methods from.
    :param prefix: The prefix to use for class names in the dictionary.
    :param visited: A set of classes that have already been visited to avoid redundancy.
    :return: A dictionary mapping class names to their methods.
    """
    if visited is None:
        visited = set()

    methods_dict = {}
    if cls in visited:
        return methods_dict

    visited.add(cls)

    methods_dict[prefix] = get_methods_from_class(cls)
    for name, obj in inspect.getmembers(cls, inspect.isclass):
        full_name = f"{prefix}.{name}" if prefix else name
        methods_dict.update(recursive_collect_methods(obj, full_name, visited))
    return methods_dict


def get_all_methods(module: str, root_class_name: str) -> Dict[str, List[str]]:
    """
    Retrieve all methods from the specified module's root class and its nested classes.

    :usage: methods = get_all_methods('models', 'api')

    :param module: The module name where the root class is defined.
    :param root_class_name: The name of the root class to analyze.
    :return: A dictionary mapping class names to their methods.
    """
    import_module = __import__(module, fromlist=[root_class_name])
    root_class = getattr(import_module, root_class_name)
    return recursive_collect_methods(root_class)


class TestUDP_API_ASCII(unittest.TestCase):
    def setUp(self):
        self.local_ip = ip.ip_address("192.168.3.100")
        self.local_port = 50000
        self.dest_ip = ip.ip_address("192.168.3.110")
        self.dest_port = 50000
        self.args = (self.local_ip, self.local_port, self.dest_ip, self.dest_port)
        self.speed = 0.01

        print(*self.args)

    def test_get_input_gain(self):
        response = UDP.send(*self.args, ASCII.get.input.gain(0))
        self.assertEqual(ASCII.get.input.gain(0), response)

    def test_get_input_gains(self):
        response = UDP.send(*self.args, ASCII.get.input.gains(0, 1))
        self.assertIn(ASCII.get.input.gains(0, 1), response)

    def test_get_input_level(self):
        response = UDP.send(*self.args, ASCII.get.input.level(0))
        self.assertEqual(ASCII.get.input.level(0), response)

    def test_get_input_levels(self):
        response = UDP.send(*self.args, ASCII.get.input.levels(0, 1))
        self.assertIn(ASCII.get.input.levels(0, 1), response)

    def test_get_input_link(self):
        response = UDP.send(*self.args, ASCII.get.input.link(0))
        self.assertEqual(ASCII.get.input.link(0), response)

    def test_get_input_links(self):
        response = UDP.send(*self.args, ASCII.get.input.links(0, 1))
        self.assertIn(ASCII.get.input.links(0, 1), response)

    def test_get_input_mute(self):
        response = UDP.send(*self.args, ASCII.get.input.mute(0))
        self.assertEqual(ASCII.get.input.mute(0), response)

    def test_get_input_mutes(self):
        response = UDP.send(*self.args, ASCII.get.input.mutes(0, 1))
        self.assertIn(ASCII.get.input.mutes(0, 1), response)

    def test_get_input_name(self):
        response = UDP.send(*self.args, ASCII.get.input.name(0))
        self.assertEqual(ASCII.get.input.name(0), response)

    def test_get_input_names(self):
        response = UDP.send(*self.args, ASCII.get.input.names(0, 1))
        self.assertIn(ASCII.get.input.names(0, 1), response)

    def test_get_input_phantom(self):
        response = UDP.send(*self.args,
                            ASCII.get.input.phantom(0))
        self.assertEqual(ASCII.get.input.phantom(0), response)

    def test_get_input_phantoms(self):
        response = UDP.send(*self.args,
                            ASCII.get.input.phantoms(0, 1))
        self.assertIn(ASCII.get.input.phantoms(0, 1), response)

    def test_get_input_phase(self):
        response = UDP.send(*self.args, ASCII.get.input.phase(0))
        self.assertEqual(ASCII.get.input.phase(0), response)

    def test_get_input_phases(self):
        response = UDP.send(*self.args, ASCII.get.input.phases(0, 1))
        self.assertIn(ASCII.get.input.phases(0, 1), response)

    def test_get_input_sensitivity(self):
        response = UDP.send(*self.args,
                            ASCII.get.input.sensitivity(0))
        self.assertEqual(ASCII.get.input.sensitivity(0), response)

    def test_get_input_sensitivities(self):
        response = UDP.send(*self.args,
                            ASCII.get.input.sensitivities(0, 1))
        self.assertIn(ASCII.get.input.sensitivities(0, 1), response)

    def test_get_input_type(self):
        response = UDP.send(*self.args, ASCII.get.input.type(0))
        self.assertEqual(ASCII.get.input.type(0), response)

    def test_get_input_types(self):
        response = UDP.send(*self.args, ASCII.get.input.types(0, 1))
        self.assertIn(ASCII.get.input.types(0, 1), response)

    def test_get_mixer_gain(self):
        response = UDP.send(*self.args, ASCII.get.mixer.gain(0, 0))
        self.assertEqual(ASCII.get.mixer.gain(0, 0), response)

    def test_get_mixer_gain_horizontal(self):
        response = UDP.send(*self.args,
                            ASCII.get.mixer.gain_horizontal((0, 1), 0))
        self.assertEqual(ASCII.get.mixer.gain_horizontal((0, 1), 0), response)

    def test_get_mixer_gain_vertical(self):
        response = UDP.send(*self.args,
                            ASCII.get.mixer.gain_vertical(0, (0, 1)))
        self.assertEqual(ASCII.get.mixer.gain_vertical(0, (0, 1)), response)

    def test_get_mixer_switch(self):
        response = UDP.send(*self.args, ASCII.get.mixer.switch(0, 0))
        self.assertEqual(ASCII.get.mixer.switch(0, 0), response)

    def test_get_mixer_switch_horizontal(self):
        response = UDP.send(*self.args,
                            ASCII.get.mixer.switch_horizontal((0, 1), 0))
        self.assertEqual(ASCII.get.mixer.switch_horizontal((0, 1), 0), response)

    def test_get_mixer_switch_vertical(self):
        response = UDP.send(*self.args,
                            ASCII.get.mixer.switch_vertical(0, (0, 1)))
        self.assertEqual(ASCII.get.mixer.switch_vertical(0, (0, 1)), response)

    def test_get_output_gain(self):
        response = UDP.send(*self.args, ASCII.get.output.gain(0))
        self.assertEqual(ASCII.get.output.gain(0), response)

    def test_get_output_gains(self):
        response = UDP.send(*self.args,
                            ASCII.get.output.gains(0, 1))
        self.assertIn(ASCII.get.output.gains(0, 1), response)

    def test_get_output_level(self):
        response = UDP.send(*self.args, ASCII.get.output.level(0))
        self.assertEqual(ASCII.get.output.level(0), response)

    def test_get_output_levels(self):
        response = UDP.send(*self.args, ASCII.get.output.levels(0, 1))
        self.assertIn(ASCII.get.output.levels(0, 1), response)

    def test_get_output_link(self):
        response = UDP.send(*self.args, ASCII.get.output.link(0))
        self.assertEqual(ASCII.get.output.link(0), response)

    def test_get_output_links(self):
        response = UDP.send(*self.args, ASCII.get.output.links(0, 1))
        self.assertIn(ASCII.get.output.links(0, 1), response)

    def test_get_output_mute(self):
        response = UDP.send(*self.args, ASCII.get.output.mute(0))
        self.assertEqual(ASCII.get.output.mute(0), response)

    def test_get_output_mutes(self):
        response = UDP.send(*self.args, ASCII.get.output.mutes(0, 1))
        self.assertIn(ASCII.get.output.mutes(0, 1), response)

    def test_get_output_name(self):
        response = UDP.send(*self.args, ASCII.get.output.name(0))
        self.assertEqual(ASCII.get.output.name(0), response)

    def test_get_output_names(self):
        response = UDP.send(*self.args, ASCII.get.output.names(0, 1))
        self.assertIn(ASCII.get.output.names(0, 1), response)

    def test_get_output_phase(self):
        response = UDP.send(*self.args, ASCII.get.output.phase(0))
        self.assertEqual(ASCII.get.output.phase(0), response)

    def test_get_output_phases(self):
        response = UDP.send(*self.args, ASCII.get.output.phases(0, 1))
        self.assertIn(ASCII.get.output.phases(0, 1), response)

    def test_get_scene_name(self):
        response = UDP.send(*self.args, ASCII.get.scene.name(0))
        self.assertEqual(ASCII.get.scene.name(0), response)

    def test_get_scene_names(self):
        response = UDP.send(*self.args, ASCII.get.scene.names(0, 1))
        self.assertIn(ASCII.get.scene.names(0, 1), response)

    def test_get_sysctl_mute(self):
        response = UDP.send(*self.args, ASCII.get.sysctl.mute())
        self.assertEqual(ASCII.get.sysctl.mute(), response)

    def test_set_input_gain(self):
        response = UDP.send(*self.args, ASCII.set.input.gain(0, 1))
        self.assertEqual(ASCII.set.input.gain(0, 1), response)

    def test_set_input_gains(self):
        response = UDP.send(*self.args, ASCII.set.input.gains(0, 1, 1))
        self.assertEqual(ASCII.set.input.gains(0, 1, 1), response)

    def test_set_input_link(self):
        response = UDP.send(*self.args, ASCII.set.input.link(0, 1))
        self.assertEqual(ASCII.set.input.link(0, 1), response)

    def test_set_input_links(self):
        response = UDP.send(*self.args, ASCII.set.input.links(0, 1, 0))
        self.assertEqual(ASCII.set.input.links(0, 1, 0), response)

    def test_set_input_mute(self):
        response = UDP.send(*self.args, ASCII.set.input.mute(0, 1))
        self.assertEqual(ASCII.set.input.mute(0, 1), response)

    def test_set_input_mutes(self):
        response = UDP.send(*self.args, ASCII.set.input.mutes(0, 1, 1))
        self.assertEqual(ASCII.set.input.mutes(0, 1, 1), response)

    def test_set_input_name(self):
        response = UDP.send(*self.args, ASCII.set.input.name(0, "foo"))
        self.assertEqual(ASCII.set.input.name(0, "foo"), response)

    def test_set_input_names(self):
        response = UDP.send(*self.args, ASCII.set.input.names(0, 1, "bar"))
        self.assertEqual(ASCII.set.input.names(0, 1, "bar"), response)

    def test_set_input_phantom(self):
        response = UDP.send(*self.args, ASCII.set.input.phantom(0, 1))
        self.assertEqual(ASCII.set.input.phantom(0, 1), response)

    def test_set_input_phantoms(self):
        response = UDP.send(*self.args, ASCII.set.input.phantoms(0, 1, 1))
        self.assertEqual(ASCII.set.input.phantoms(0, 1, 1), response)

    def test_set_input_phase(self):
        response = UDP.send(*self.args, ASCII.set.input.phase(0, 1))
        self.assertEqual(ASCII.set.input.phase(0, 1), response)

    def test_set_input_phases(self):
        response = UDP.send(*self.args, ASCII.set.input.phases(0, 1, 1))
        self.assertEqual(ASCII.set.input.phases(0, 1, 1), response)

    def test_set_input_sensitivities(self):
        response = UDP.send(*self.args, ASCII.set.input.sensitivities(0, 1, 1))
        self.assertEqual(ASCII.set.input.sensitivities(0, 1, 1), response)

    def test_set_input_sensitivity(self):
        response = UDP.send(*self.args, ASCII.set.input.sensitivity(0, 1))
        self.assertEqual(ASCII.set.input.sensitivity(0, 1), response)

    def test_set_input_type(self):
        response = UDP.send(*self.args, ASCII.set.input.type(0, 1))
        self.assertEqual(ASCII.set.input.type(0, 1), response)

    def test_set_input_types(self):
        response = UDP.send(*self.args, ASCII.set.input.types(0, 1, 1))
        self.assertEqual(ASCII.set.input.types(0, 1, 1), response)

    def test_set_mixer_gain(self):
        response = UDP.send(*self.args, ASCII.set.mixer.gain(0, 0, 1))
        self.assertEqual(ASCII.set.mixer.gain(0, 0, 1), response)

    def test_set_mixer_gain_horizontal(self):
        response = UDP.send(*self.args, ASCII.set.mixer.gain_horizontal((0, 1), 0, 1))
        self.assertEqual(ASCII.set.mixer.gain_horizontal((0, 1), 0, 1), response)

    def test_set_mixer_gain_vertical(self):
        response = UDP.send(*self.args, ASCII.set.mixer.gain_vertical(0, (0, 1), 1))
        self.assertEqual(ASCII.set.mixer.gain_vertical(0, (0, 1), 1), response)

    def test_set_mixer_switch(self):
        response = UDP.send(*self.args, ASCII.set.mixer.switch(0, 0, 1))
        self.assertEqual(ASCII.set.mixer.switch(0, 0, 1), response)

    def test_set_mixer_switch_horizontal(self):
        response = UDP.send(*self.args, ASCII.set.mixer.switch_horizontal((0, 1), 0, 1))
        self.assertEqual(ASCII.set.mixer.switch_horizontal((0, 1), 0, 1), response)

    def test_set_mixer_switch_vertical(self):
        response = UDP.send(*self.args, ASCII.set.mixer.switch_vertical(0, (0, 1), 1))
        self.assertEqual(ASCII.set.mixer.switch_vertical(0, (0, 1), 1), response)

    def test_set_output_gain(self):
        response = UDP.send(*self.args, ASCII.set.output.gain(0, 1))
        self.assertEqual(ASCII.set.output.gain(0, 1), response)

    def test_set_output_gains(self):
        response = UDP.send(*self.args, ASCII.set.output.gains(0, 1, 1))
        self.assertEqual(ASCII.set.output.gains(0, 1, 1), response)

    def test_set_output_link(self):
        response = UDP.send(*self.args, ASCII.set.output.link(0, 1))
        self.assertEqual(ASCII.set.output.link(0, 1), response)

    def test_set_output_links(self):
        response = UDP.send(*self.args, ASCII.set.output.links(0, 1, 1))
        self.assertEqual(ASCII.set.output.links(0, 1, 1), response)

    def test_set_output_mute(self):
        response = UDP.send(*self.args, ASCII.set.output.mute(0, 1))
        self.assertEqual(ASCII.set.output.mute(0, 1), response)

    def test_set_output_mutes(self):
        response = UDP.send(*self.args, ASCII.set.output.mutes(0, 1, 1))
        self.assertEqual(ASCII.set.output.mutes(0, 1, 1), response)

    def test_set_output_name(self):
        response = UDP.send(*self.args, ASCII.set.output.name(0, "foo"))
        self.assertEqual(ASCII.set.output.name(0, "foo"), response)

    def test_set_output_names(self):
        response = UDP.send(*self.args, ASCII.set.output.names(0, 1, "bar"))
        self.assertEqual(ASCII.set.output.names(0, 1, "bar"), response)

    def test_set_output_phase(self):
        response = UDP.send(*self.args, ASCII.set.output.phase(0, 1))
        self.assertEqual(ASCII.set.output.phase(0, 1), response)

    def test_set_output_phases(self):
        response = UDP.send(*self.args, ASCII.set.output.phases(0, 1, 1))
        self.assertEqual(ASCII.set.output.phases(0, 1, 1), response)

    def test_set_scene_name(self):
        response = UDP.send(*self.args, ASCII.set.scene.name(0, "foo"))
        self.assertEqual(ASCII.set.scene.name(0, "foo"), response)

    def test_set_scene_names(self):
        response = UDP.send(*self.args, ASCII.set.scene.names(0, 1, "bar"))
        self.assertEqual(ASCII.set.scene.names(0, 1, "bar"), response)

    def test_set_sysctl_mute(self):
        response = UDP.send(*self.args, ASCII.set.sysctl.mute(1))
        self.assertEqual(ASCII.set.sysctl.mute(1), response)

    def test_scene_save(self):
        response = UDP.send(*self.args, ASCII.scene.save(0))
        self.assertEqual(ASCII.scene.save(0), response)

    def test_scene_toggle(self):
        response = UDP.send(*self.args, ASCII.scene.toggle(0))
        self.assertEqual(ASCII.scene.toggle(0), response)
