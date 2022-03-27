import numpy as np
import Tensor4Me as t4m

title_ = "Forward"
in_ = 0.5


def test_(x):
    A = t4m.Function.Square()
    B = t4m.Function.Exp()
    C = t4m.Function.Square()

    x = t4m.Variable(np.array(x))
    a = A(x)
    b = B(a)
    y = C(b)
    return y.data


def valid_(x):
    return np.exp(x ** 2) ** 2
