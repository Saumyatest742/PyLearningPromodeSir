class Calc:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
output = object_ref.sum(10, 20)
output2 = object_ref.sub(40, 20)
output3 = object_ref.mul(34, 20)
output4 = object_ref.div(100, 20)
print(output)
print(output2)
print(output3)
print(output4)
