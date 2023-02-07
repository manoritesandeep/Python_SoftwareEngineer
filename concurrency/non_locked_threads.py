"""
An `atomic operation` is one that cannot be interrupted in the middle of it.
Eg: a Print statement cannot print half the line and then be interrupted

The technique of adding random sleeps between statements
when you're doing multi-threading codes is called `fuzzing`.
It lets us see problems
"""

import time
import random
from threading import Thread

counter = 0

def increment_counter():
    global counter
    # add random weights
    time.sleep(random.random())
    counter +=1
    print(f"New counter value: {counter}")
    time.sleep(random.random())
    print('-----------')

for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()

