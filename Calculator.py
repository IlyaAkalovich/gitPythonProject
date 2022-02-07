class Calculator:

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def enter(self):
        inp = input("Введите выражение: ")
        self.a = int(inp[0])
        self.sign = inp[1]
        self.b = int(inp[2])

    def calculate(self):
        if self.sign == "+":
            return self.add()
        elif self.sign == "-":
            return self.subtract()
        elif self.sign == "*":
            return self.multiply()
        elif self.sign == "/":

            try:
                return self.divide()
            except ZeroDivisionError:
                return "деление на ноль невозможно"


calc = Calculator()
calc.enter()
print("первое число: ", calc.a)
print("знак: ", calc.sign)
print("второе число: ", calc.b)
print("Результат: ",calc.calculate())

