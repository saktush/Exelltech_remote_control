class A:
    def __init__(self):
        self._a = 0
        self._ls = [1, 2, 3]

    @property
    def a(self):
        return self._a

    # @a.setter
    # def a(self, v):
    #     self._a = v

    @property
    def ls(self):
        return self._ls


my_a = A()
print(my_a.a)

print(my_a.a)

print("---".center)

print(my_a.ls)
my_a.ls.clear()
print(my_a.ls)

