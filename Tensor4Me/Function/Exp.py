import numpy as np
from .Base import Base


class Exp(Base):
    def forward(self, x):
        return np.exp(x)

    def backward(self, gradient):
        x = self.variable.data
        return np.exp(x) * gradient
