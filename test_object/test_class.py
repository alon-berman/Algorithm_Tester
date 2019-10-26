import os.path
from Utils.utils_functions import *
import logging


def init_logger():
    """
    A simple logger to log all info printed into a file.
    :return:
    """
    logger = logging.getLogger()
    sh_handler = logging.StreamHandler()
    fh_handler = logging.FileHandler(filename='algorithm_test.log')
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    sh_handler.setFormatter(formatter)
    fh_handler.setFormatter(formatter)
    logger.addHandler(sh_handler)
    logger.addHandler(fh_handler)
    logger.setLevel(logging.DEBUG)


class TestObject:
    """
    This object is responsible to init, load, run, and write a single algorithm test.
    """
    def __init__(self, test_number, data):
        init_logger()
        self.test_number = test_number
        self.test_name = data['test_name']
        self.algorithm_file_path = data['algorithm_file_path']
        self.algorithm_function_name = data['algorithm_function_name']
        self.module_input_args = data['module_input_args']
        self.csv_path = data['result_csv_path']
        self.parameter_modules_paths = data['parameter_modules']
        self.parameter_modules = load_parameter_modules(self.parameter_modules_paths)
        self.algo_func = self.load_algorithm()
        self.init_csv()
        self.run_test()

    def load_algorithm(self):
        """
        this function loads the main algorithm
        :return:
        """
        logging.info("loading algorithm {} from {}".format(self.test_name, self.algorithm_file_path))
        return load_single_module(self.algorithm_file_path, self.algorithm_function_name)

    def write_to_csv(self, line):
        """
        write a single line in a csv file.
        :param line: the line to be written
        :return:
        """
        f = open(self.csv_path, 'a+')
        f.write(str(line) + '\n')
        f.close()

    def run_test(self):
        """
        the core function to evaluate each test case. it will
        :return:
        """
        for ind, module in enumerate(self.parameter_modules):
            eval_str = 'algo_func('
            if not self.module_input_args:  # in case function doesn't need input args.
                eval_str += str(module())
            else:
                for arg in self.module_input_args:
                    eval_str += str(module(arg)) + ','
            eval_str += ')'
            res = eval(eval_str, {'algo_func': self.algo_func})
            self.write_to_csv('{},{},{},{},{}'
                              .format(self.test_number,
                                      self.algorithm_function_name,
                                      self.parameter_modules_paths[ind],
                                      self.module_input_args,
                                      res))
            eval_str = ''  # reset eval string for next iteration

    def init_csv(self):
        """
        appends headers to the csv in case the file was newly created
        :return:
        """
        if os.path.isfile(self.csv_path):
            pass
        else:
            self.write_to_csv('Test Number, Algorithm Function Name, Used Module, Module Input Args, Final Result')
