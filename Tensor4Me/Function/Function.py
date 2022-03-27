import abc
import Tensor4Me as t4m

class Function(object, metaclass=abc.ABCMeta):
    def __call__(self, variable: t4m.Variable):
        self.__set_variable(variable)

        x = variable.get_data()
        y = self.forward(x)
        return t4m.Variable(y)

    def __set_variable(self, variable: t4m.Variable):
        self.__variable 

    @abc.abstractmethod
    def forward(self, x):
        pass

    @abc.abstractmethod
    def backward(self, x):
        pass