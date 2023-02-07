from collections import deque
from types import coroutine

friends = deque(('Mandeep', 'Josh', 'Hemant','Jose'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")


async def greet(g):
    print("Starting...")
    await g     # same as yield from
    print("Ending...")


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("Hello")
print("Hello, world! Multitasking...")
# greeter.send("How are you?")
# greeter.send("How are you?")
# greeter.send("How are you?")
# greeter.send("How are you?")
greeting = input("Enter a greeting: ")
greeter.send(greeting)
greeting = input("Enter a greeting: ")
greeter.send(greeting)
greeting = input("Enter a greeting: ")
greeter.send(greeting)