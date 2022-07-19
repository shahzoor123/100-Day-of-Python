class Calculator:

    def __init__(self):
        self.total = 0

    def add(self, n1, n2):
        self.total = n1 + n2
        return self.total

    def sub(self, n1, n2):
        self.total = n1 - n2
        return self.total

    def mul(self, n1, n2):
        self.total = n1 * n2
        return self.total

    def div(self, n1, n2):
        self.total = n1 / n2
        return self.total
