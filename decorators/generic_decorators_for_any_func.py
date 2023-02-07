user = {
    'id': 1,
    'name': 'Rahul',
    'role': 'admin'
}
import functools


def get_perms(func):
    @functools.wraps(func)
    def secure(*args, **kwargs):
        if user.get('role') == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('You are not admin.')

    return secure


@get_perms
def is_pwd(panel):
    return f"The admin password for {panel} is 123456789"


print(is_pwd('movies'))
