from immutableType import *


class operation():

    @callable_(args_types=[int], is_class=True)
    def __init__(self, num1, num2):
        self.num1 = Int_(num1)
        self.num2 = Int_(num2)

    def add(self):
        return self.num1.int_ + self.num2.int_

    @callable_(args_types=[int], is_class=True)
    def change_num1(self, newNum):

        self.num1.int_ = newNum


op = operation(1, 4)
print(op.add())
op.change_num1(True)