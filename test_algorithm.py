import argparse
from test_object.TestObjects import TestObject
from Utils.util_functions import parse_json


def parse_outer_args():
    """
    This function parses CMD parameter given by user
    :return: arguments as dict
    """
    parser = argparse.ArgumentParser(description='Evaluate different modules using the dynamic test case'
                                                 ' infrastructure')
    parser.add_argument('--path', help="provide absolute path to json test case", type=str)
    args = parser.parse_args()
    return args


def run_all_tests(json_path):
    """
    the main entry point to the tester. it will first parse the json file, and assign a Test object to each test case
    defined in the json
    :param json_path: absolute path to a JSON file
    :return: -
    """
    print('Starting Test Sequence ...')
    # parse JSON
    tests_data = parse_json(json_path)
    # append test cases to test suite
    for test_ind, single_test_data in enumerate(tests_data):
        TestObject(test_ind+1, single_test_data)
        print('Done Test {} out of {}'.format(test_ind+1, len(tests_data)))
    print('Finished Testing! you may see results at {}'.format(tests_data[0]['result_csv_path']))


if __name__ == '__main__':
    outer_args = parse_outer_args()
    run_all_tests(r"C:\Git\algorithm_tester\Config\TestsJsonFileExample.json")

