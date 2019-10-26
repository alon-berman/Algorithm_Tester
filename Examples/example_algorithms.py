import numpy as np


def run_pythagorean_algo(a, b):
    """
    the example provided
    :param a:
    :param b:
    :return:
    """
    return np.sqrt(ad(a, b))


def ad(a, b):
    return a + b


def p2(num):
    return num * num


def get_circle_radius_from_surface(surface):
    """
    just another example for a different "algorithm"
    :param surface:
    :return:
    """
    return np.sqrt(surface / np.pi)


def no_input_args_func():
    """
    made for testing purposes
    :return:
    """
    return 5


if __name__ == '__main__':
    num_1 = 6
    num_2 = 3
    p_of_num1 = p2(num_1)
    p_of_num2 = p2(num_2)
    res = run_pythagorean_algo(p_of_num1, p_of_num2)

    print("result is: {}. input args = {}"
          .format(res, [num_1, num_2]))