import importlib.util
import logging
import os
import sys
from test_object.TestExceptions import TestException


def load_parameter_modules(modules_list):
    """
    load all modules defined in JSON file under "parameter_modules" field. i.e. load different 'p2'
    functions in the example given.
    :param modules_list: a list of paths retrieved from the JSON file under "parameter_modules"
    :return:
    """
    imported_modules = []
    for module in modules_list:
        try:
            logging.info('importing function {} from {}'.format(module[1], module[0]))
            imported_modules.append(load_single_module(module[0], module[1]))
        except Exception as e:
            raise TestException('Failed to import function!. details: {}'.format(e), 3)
    return imported_modules


def load_single_module(path, func_name):
    """
    this function loads a function from pythonic module, which later will be evaluated.
    :param path: path to file where function is stored
    :param func_name: the function name
    :return: the function to be evaluated
    """
    try:
        curr_dir = os.path.dirname(path)
        sys.path.append(os.path.abspath(curr_dir))
        spec = importlib.util.spec_from_file_location(func_name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return getattr(module, func_name)
    except Exception as e:
        raise TestException('Failed to import function!. details: {}'.format(e), 3)


def parse_json(path):
    """
    simple function to parse a json file
    :param path: path to file including suffix.
    :return: parsed json object
    """
    import json
    try:
        with open(path, 'r') as file:
            test_data = file.read()
        return json.loads(test_data)
    except Exception as e:
        raise TestException('Failed to load JSON file!. details: {}\n System will now terminate ....'
                            .format(e), 3, terminate=True)
