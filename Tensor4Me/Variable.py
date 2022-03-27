class Variable(object):
    def __init__(self, data):
        # Do not implement until actual needs!
        self.data = data
        self.grad = None
        self.creator = None

    def backward(self):
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)
