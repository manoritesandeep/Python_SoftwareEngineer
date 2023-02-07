from addition import Addition

class Calculator:
    @classmethod
    def add(cls, value1, value2):
        return Addition.add(value1, value2)

    @classmethod
    def subtract(cls, value1, value2):
        return cls.add(value1, -value2)

    @classmethod
    def multiply(cls, value1, value2):
        result = 0
        for i in range(0, value2):
            result = result + value1
        return result

    @classmethod
    def divide(cls, value1, value2):
        res = 0
        while value1>=value2:
            value1 = cls.subtract(value1, value2)
            res = cls.add(res, 1)
        return res

print(Calculator.add(9,1))
print(Calculator.subtract(12,1))
print(Calculator.multiply(12,1))
print(Calculator.divide(26,2))