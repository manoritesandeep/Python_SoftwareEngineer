"""
Taken from our Complete Python Course: https://www.udemy.com/the-complete-python-course/?couponCode=REPLIT

Purely as an example, a function can have multiple decorators.

Decorators are applied from bottom to top, which means the top decorator is the first one to be evaluated when the function is executed.

In this example, we have two decorators. One checks the user's access_level, the other checks the user's username (must start with the letter 'j').
"""

import functools

# Try the various combinations below!
user = {'username': 'jose123', 'access_level': 'admin'}


# user = {'username': 'bob', 'access_level': 'admin'}
# user = {'username': 'jose123', 'access_level': 'user'}
# user = {'username': 'bob', 'access_level': 'user'}

def user_name_starts_with_j(func):
    """
    This decorator only runs if the function passed the user's username starts with a j.
    """

    @functools.wraps(func)
    def secure(*args, **kwargs):
        if user.get('username').startswith('j'):
            return func(*args, **kwargs)
        else:
            raise PermissionError("Name does not start with J, access denied!")

    return secure


def user_permissions(func):
    """
    This decorators checks the user permissions and access levels
    """

    @functools.wraps(func)
    def secure(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError("Access denied!")

    return secure


@user_permissions
@user_name_starts_with_j
def double_decorator():
    return 'I ran successfully!'


print(double_decorator())

"""
When `double_decorator()` runs, this chain of "functions" runs:
user_has_permission -> user_name_starts_with_j -> double_decorator
That is because `user_name_starts_with_j` is the first decorator to be applied. 
It replaces `double_decorator` by the function it returns.
Then, `user_has_permission` is applied—and it replaces the function the other decorator 
returned by the function it returns.
"""
