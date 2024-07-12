import inspect
from types import FunctionType
from typing import Type, List, Dict, Optional, Set


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


# Example usage:
if __name__ == '__main__':
    methods = get_all_methods('models', 'api')
    for class_name, methods in methods.items():
        for method in methods:
            print(f"Class {class_name} has method: {method}")
