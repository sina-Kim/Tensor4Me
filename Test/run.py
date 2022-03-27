import sys

sys.path.append("C:\\Users\\sinakim\\Tensor4Me")
import numpy as np
import Tensor4Me as t4m


def error(a, b):
    return abs(a - b) < 1e-5


def forward_test(x, func):
    A = t4m.Function.Square()
    B = t4m.Function.Exp()
    C = t4m.Function.Square()

    _x = t4m.Variable(np.array(x))
    a = A(_x)
    b = B(a)
    _y = C(b)
    return error(func(x), _y.data)


def forward_valid(x):
    return np.exp(x ** 2) ** 2


if __name__ == "__main__":

    test_list = [
        {"title": "Forward", "func": forward_test, "valid": forward_valid, "in": 0.5,}
    ]

    for test_element in test_list:
        print(
            'Test "{}": {}'.format(
                test_element["title"],
                test_element["func"](test_element["in"], test_element["valid"]),
            )
        )
