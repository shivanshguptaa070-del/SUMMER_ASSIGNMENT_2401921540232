class MyQueue(object):
    
    def __init__(self):
        self.i = []
        self.o = []
        self.p = None

    def push(self, x):
        if len(self.i) == 0:
            self.p = x
        self.i.append(x)

    def pop(self):
        if len(self.o) == 0:
            while len(self.i) > 0:
                x = self.i.pop()
                self.o.append(x)
        return self.o.pop()

    def peek(self):
        if len(self.o) > 0:
            return self.o[-1]
        return self.p

    def empty(self):
        return len(self.i) == 0 and len(self.o) == 0