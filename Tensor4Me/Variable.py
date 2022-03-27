class Variable(object):
    def __init__(self, data):
        self.set_data(data)
        self.__grad = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data