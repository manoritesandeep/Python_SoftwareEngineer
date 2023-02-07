# Using generators is another way of achieving multi-tasking in Python
def countdown(n):
    while n>0:
        yield n
        n -= 1

c1 = countdown(10)
c2 = countdown(20)
print(next(c1))  # 10
print(next(c2))  # 20
print(next(c1))  # 9
print(next(c2))  # 19
