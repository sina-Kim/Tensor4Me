import numpy as np
import Tensor4Me as t4m

class Exp(t4m.Function.Base):
    def forward(self, x):
        return np.exp(x)

    def backward(self, gradient):
        x = self.variable.data
        return np.exp(x) * gradient