class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b > 0:
            for i in range(b):
                result = self.add(result, a)
        elif a > 0:
            for i in range(a):
                result = self.add(result, b)
        else:
            x = self.subtract(result, a)
            y = self.subtract(result, b)
            for i in range(x):
                result = self.add(result, y)
        return result
            
    def divide(self, a, b):
        result = 0

        if b == 0:
            return "Can not divie!!"
        
        negative = (a < 0) != (b < 0)

        if a < 0:
            a = self.subtract(0, a)

        if b < 0:
            b = self.subtract(0, b)

        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if negative:
            result = self.subtract(0, result)

        return result

    def modulo(self, a, b):
        if b == 0:
            return"Can not modulo"

        negative = a < 0

        if a < 0:
            a = self.subtract(0, a)

        if b < 0:
            b = self.subtract(0, b)

        while a >= b:
            a = self.subtract(a, b)

        if negative:
            a = self.subtract(0, a)

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))