user1 = {
    'id': 1,
    'name': 'Mandy',
    'role': 'admin'
}


def check_user_permission(func):
    def secure():
        if user1.get('role') == 'admin':
            return func()
        else:
            raise PermissionError("You are not an admin")

    return secure


def admin_password():
    return "The admin password is 1234."


get_password = check_user_permission(admin_password)
print(get_password())
