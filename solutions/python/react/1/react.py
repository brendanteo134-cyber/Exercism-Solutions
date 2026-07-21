from functools import partial
class InputCell(object):
    def __init__(self, initial_value):
        self._callbacks = []
        self._value = initial_value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
        for c in self._callbacks:
            c(self._value)
class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self._callbacks = []
        self._value = None
        self._inputs = [_input.value for _input in inputs]
        self._compute_function = compute_function
        self.value = self._compute_function(self._inputs)
        for i, _input in enumerate(inputs):
            _input._callbacks.append(partial(self.update, index=i))
    def update(self, value, index):
        self._inputs[index] = value
        if index == len(self._inputs) - 1:
            self.value = self._compute_function(self._inputs)
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if self._value != value:
            for c in self._callbacks:
                c(value)
        self._value = value
    def add_callback(self, callback):
        self._callbacks.append(callback)
    def remove_callback(self, callback):
        try:
            self._callbacks.remove(callback)
        except ValueError:
            pass
