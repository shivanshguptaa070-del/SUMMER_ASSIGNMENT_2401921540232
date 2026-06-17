class MinStack(object):
    def __init__(self):
        self.s = []
        self.m = []
    def push(self, x):
        self.s.append(x)
        if self.m == []:
            self.m.append(x)
        else:
            if x < self.m[-1]:
                self.m.append(x)
            else:
                self.m.append(self.m[-1])
    def pop(self):
        self.s.pop()
        self.m.pop()
    def top(self):
        return self.s[-1]
    def getMin(self):
        return self.m[-1]