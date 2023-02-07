import functools

user = {
    'id': 1,
    'name': 'Bam_Slam',
    'role': 'admin'
}


def check_user_perms(func):
    @functools.wraps(func)
    def secure():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError("Not an admin.")

    return secure


@check_user_perms
def admin_pass():
    """
    Allows us to retrieve the password for the admin panel.
    """
    return "The admin password is 12345"


print(admin_pass())
# print(admin_pass.__name__)  # return secure since function is replaced by secure()
# print(admin_pass.__doc__)   #returns none since its replaced by secure.
# to avoid above issues we use functools, that keeps the name and doc string, etc
print(admin_pass.__doc__)
print(admin_pass.__name__)
