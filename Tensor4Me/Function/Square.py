import Tensor4Me as t4m

class Square(t4m.Function.Base):
    def forward(self, x):
        return x ** 2

    def backward(self, gradient):
        x = self.variable.data
        return 2 * x * gradient