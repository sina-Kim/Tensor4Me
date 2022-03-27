import abc
import Tensor4Me as t4m

class Function(object, metaclass=abc.ABCMeta):
    def __call__(self, variable: t4m.Variable):
        self.variable = variable
        x = variable.data
        y = self.forward(x)
        return t4m.Variable(y)

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, x):
        raise NotImplementedError()