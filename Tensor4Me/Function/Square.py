from .Base import Base


class Square(Base):
    def forward(self, x):
        return x ** 2

    def backward(self, gradient):
        x = self.variable.data
        return 2 * x * gradient
