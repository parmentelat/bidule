from .helpers import helper

class Machine:
    def __init__(self):
        self.name = helper()
        self._state = 'off'

    def __repr__(self):
        return f'{self.name} is {self._state}'
