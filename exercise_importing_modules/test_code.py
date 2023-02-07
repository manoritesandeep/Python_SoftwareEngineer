def multiply(value1, value2):
    result = 0
    for i in range(0, value2):
        result = result + value1
    return result

print(multiply(3,4))

def divide(value1, value2):
    res = 0
    while value1 >= value2:
        value1 = value1 -value2
        res = res + 1
    return res
print(divide(12,3))
