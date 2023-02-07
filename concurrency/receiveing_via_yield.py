# Example 1
def greet():
    friend = yield
    print(f"Hello, {friend}")

g = greet()
g.send(None)    #priming the generator
g.send("Adam")

# Example 2

from collections import deque

friends = deque(('Mandeep', 'Josh', 'Hemant','Jose'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

# def greet(g):
#     g.send(None)
#     while True:
#         greeting = yield
#         g.send(greeting)

## or
def greet(g):
    yield from g


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hello")
print("Hello, world! Multitasking...")
greeter.send("How are you?")

"""
When we have generators that receive data,
they're really no longer called generators
because they're not generating anything rather receiving data.
Since, they're receiving data and doing something with it.
So, this type of generator shall be known as a co-routine.
"""