import inspect
import time
import unittest
from types import FunctionType
from typing import Type, List, Dict, Optional, Set
from modules.api import ASCII
from modules.system import UDP
from config import LOCAL_IP, LOCAL_PORT, REMOTE_IP, REMOTE_PORT

"""
! Don't forget to check /config.py for IP and Port settings
"""


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

    :usage: methods = get_all_methods('modules', 'api')

    :param module: The module name where the root class is defined.
    :param root_class_name: The name of the root class to analyze.
    :return: A dictionary mapping class names to their methods.
    """
    import_module = __import__(module, fromlist=[root_class_name])
    root_class = getattr(import_module, root_class_name)
    return recursive_collect_methods(root_class)


class TestUDP_API_ASCII(unittest.TestCase):
    def setUp(self):
        self.dest_ip = REMOTE_IP
        self.dest_port = REMOTE_PORT
        self.args = (LOCAL_IP, LOCAL_PORT, self.dest_ip, self.dest_port)
        # cooldown time
        self.speed = 0.025

    def tearDown(self):
        time.sleep(self.speed)

    def test_get_input_gain(self):
        command: str = ASCII.get.input.gain(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_gains(self):
        command: str = ASCII.get.input.gains(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_level(self):
        command: str = ASCII.get.input.level(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_levels(self):
        command: str = ASCII.get.input.levels(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_link(self):
        command: str = ASCII.get.input.link(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_links(self):
        command: str = ASCII.get.input.links(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_mute(self):
        command: str = ASCII.get.input.mute(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_mutes(self):
        command: str = ASCII.get.input.mutes(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_name(self):
        command: str = ASCII.get.input.name(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_names(self):
        command: str = ASCII.get.input.names(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_phantom(self):
        command: str = ASCII.get.input.phantom(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_phantoms(self):
        command: str = ASCII.get.input.phantoms(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_phase(self):
        command: str = ASCII.get.input.phase(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_phases(self):
        command: str = ASCII.get.input.phases(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_sensitivity(self):
        command: str = ASCII.get.input.sensitivity(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_sensitivities(self):
        command: str = ASCII.get.input.sensitivities(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_type(self):
        command: str = ASCII.get.input.type(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_input_types(self):
        command: str = ASCII.get.input.types(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_gain(self):
        command: str = ASCII.get.mixer.gain(0, 0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_gain_horizontal(self):
        command: str = ASCII.get.mixer.gain_horizontal((0, 1), 0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_gain_vertical(self):
        command: str = ASCII.get.mixer.gain_vertical(0, (0, 1))
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_switch(self):
        command: str = ASCII.get.mixer.switch(0, 0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_switch_horizontal(self):
        command: str = ASCII.get.mixer.switch_horizontal((0, 1), 0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_mixer_switch_vertical(self):
        command: str = ASCII.get.mixer.switch_vertical(0, (0, 1))
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_gain(self):
        command: str = ASCII.get.output.gain(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_gains(self):
        command: str = ASCII.get.output.gains(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_level(self):
        command: str = ASCII.get.output.level(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_link(self):
        command: str = ASCII.get.output.link(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_links(self):
        command: str = ASCII.get.output.links(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_mute(self):
        command: str = ASCII.get.output.mute(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_mutes(self):
        command: str = ASCII.get.output.mutes(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_name(self):
        command: str = ASCII.get.output.name(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_names(self):
        command: str = ASCII.get.output.names(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_phase(self):
        command: str = ASCII.get.output.phase(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_output_phases(self):
        command: str = ASCII.get.output.phases(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_scene_name(self):
        command: str = ASCII.get.scene.name(0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_scene_names(self):
        command: str = ASCII.get.scene.names(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_get_sysctl_mute(self):
        command: str = ASCII.get.sysctl.mute()
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_gain(self):
        command: str = ASCII.set.input.gain(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_gains(self):
        command: str = ASCII.set.input.gains(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_link(self):
        command: str = ASCII.set.input.link(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_links(self):
        command: str = ASCII.set.input.links(0, 1, 0)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_mute(self):
        command: str = ASCII.set.input.mute(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_mutes(self):
        command: str = ASCII.set.input.mutes(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_name(self):
        command: str = ASCII.set.input.name(0, "foo")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_names(self):
        command: str = ASCII.set.input.names(0, 1, "bar")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_phantom(self):
        command: str = ASCII.set.input.phantom(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_phantoms(self):
        command: str = ASCII.set.input.phantoms(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_phase(self):
        command: str = ASCII.set.input.phase(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_phases(self):
        command: str = ASCII.set.input.phases(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_sensitivities(self):
        command: str = ASCII.set.input.sensitivities(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_sensitivity(self):
        command: str = ASCII.set.input.sensitivity(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_type(self):
        command: str = ASCII.set.input.type(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_input_types(self):
        command: str = ASCII.set.input.types(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_gain(self):
        command: str = ASCII.set.mixer.gain(0, 0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_gain_horizontal(self):
        command: str = ASCII.set.mixer.gain_horizontal((0, 1), 0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_gain_vertical(self):
        command: str = ASCII.set.mixer.gain_vertical(0, (0, 1), 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_switch(self):
        command: str = ASCII.set.mixer.switch(0, 0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_switch_horizontal(self):
        command: str = ASCII.set.mixer.switch_horizontal((0, 1), 0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_mixer_switch_vertical(self):
        command: str = ASCII.set.mixer.switch_vertical(0, (0, 1), 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_gain(self):
        command: str = ASCII.set.output.gain(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_gains(self):
        command: str = ASCII.set.output.gains(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_link(self):
        command: str = ASCII.set.output.link(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_links(self):
        command: str = ASCII.set.output.links(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_mute(self):
        command: str = ASCII.set.output.mute(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_mutes(self):
        command: str = ASCII.set.output.mutes(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_name(self):
        command: str = ASCII.set.output.name(0, "foo")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_names(self):
        command: str = ASCII.set.output.names(0, 1, "bar")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_phase(self):
        command: str = ASCII.set.output.phase(0, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_output_phases(self):
        command: str = ASCII.set.output.phases(0, 1, 1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_scene_name(self):
        command: str = ASCII.set.scene.name(0, "foo")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_scene_names(self):
        command: str = ASCII.set.scene.names(0, 1, "bar")
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_set_sysctl_mute(self):
        command: str = ASCII.set.sysctl.mute(1)
        response: str = UDP.send(*self.args, command)
        self.assertIn(command, response)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_scene_save(self):
        command: str = ASCII.scene.save(0)
        response: str = UDP.send(*self.args, command)
        self.assertIsNone(response)
        time.sleep(0.25)
        print(f"Command: {command} \n"
              f"Results: {response} ")

    def test_scene_toggle(self):
        command: str = ASCII.scene.toggle(0)
        response: str = UDP.send(*self.args, command)
        print(f"Command: {command} \n"
              f"Results: {response} ")
        # time to get scene loaded
        time.sleep(1.5)
        self.assertIsNone(response)

    def test_x_set_rescene(self):
        command: str = ASCII.set.rescene()
        response: str = UDP.send(*self.args, command)
        self.assertIsNone(response)
        print(f"Command: {command} \n"
              f"Results: {response} ")


if __name__ == '__main__':
    unittest.main(verbosity=2)
