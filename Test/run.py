import sys

sys.path.append("C:\\Users\\sinakim\\Tensor4Me")


def error(a, b):
    return abs(a - b) < 1e-5


def test(f1, f2, _in):
    return error(f1(_in), f2(_in))


if __name__ == "__main__":
    module_list = ["forward"]

    test_list = []
    for module_name in module_list:
        mod = __import__(module_name, fromlist=[module_name])
        test_list.append(
            {
                "title": getattr(mod, "title_"),
                "test": getattr(mod, "test_"),
                "valid": getattr(mod, "valid_"),
                "in": getattr(mod, "in_"),
            }
        )

    for el in test_list:
        print(
            'Test "{}": {}'.format(
                el["title"], test(el["test"], el["valid"], el["in"]),
            )
        )
