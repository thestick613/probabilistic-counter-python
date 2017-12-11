import random


class MockCounter(object):
    def __init__(self):
        self.v = 0.0

    def inc(self, value):
        self.v += value

    def get(self):
        return self.v


class ProbCounter(object):
    def __init__(self, param=0.000195):
        """ Create a Probabilistic Counter object, and initialize it with the
        desired error rate, which is 1% by default (0.0002).
        """

        self.occurences = {}
        self.actions_inc = {}
        self.actions_get = {}
        self.inc_ops = 0
        self.get_ops = 0
        self.calls = 0

        self.param = param

    def create(self, name, fun_inc, fun_get):
        self.occurences[name] = 0
        self.actions_inc[name] = fun_inc
        self.actions_get[name] = fun_get

    def inc(self, name, value=1.0):
        self.calls = 1
        self.occurences[name] += 1

        b = 1.0 / (self.param * self.occurences[name] + 1.0)

        if random.random() < b:
            self.actions_inc[name](value/b)
            self.inc_ops += 1

    def get(self, name):
        vget = self.actions_get[name]()
        self.occurences[name] = int(vget)
        self.get_ops += 1

        return int(vget)
