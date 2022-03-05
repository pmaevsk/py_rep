class A:
    def __init__(self, num):
        self.num = num

    def __add__(self, b):
        c = A(self.num + b)
        return c.num


a = A(5)
print(a + 10)
