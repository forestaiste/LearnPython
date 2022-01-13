
class MyClass:
    i = 123

    def __init__(self, name, score):
        self.__name = name
        self._score = score

    def f(self):
        self.i += 1
        return self.i

    def info(self):
        print(f'student: {self.__name}; score: {self._score}')


my = MyClass('tom', 12)
print(my.i)
print(my.f())
my.info()

