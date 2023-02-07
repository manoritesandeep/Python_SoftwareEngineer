import functools

user = {
    'id': 1,
    'name': 'Jimmy',
    'role': 'admin'
}


def check_level(role):
    def get_pass(func):
        @functools.wraps(func)
        def secure(panel):
            if user.get('role') == role:
                return func(panel)
            else:
                raise PermissionError('Not an admin.')

        return secure

    return get_pass


@check_level('admin')
def admin_password(panel):
    """
    This function returns the admin password.
    """
    return f"The admin password for {panel} panel is 123456"


print(admin_password.__doc__)
print(admin_password('NBA'))
