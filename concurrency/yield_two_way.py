# Yield from another iterator in Python
from collections import deque

friends = deque(('Mandeep', 'Josh', 'Hemant','Jose'))

def get_friend():
    yield from friends

# c = get_friend()
# print(next(c))
# print(next(c))


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f"Hello, {friend}"
        except StopIteration:
            pass

friends_gen = get_friend()
g = greet(friends_gen)
print(next(g))
print(next(g))