# accept any number of positional arguments
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3, 4))


# accept any number of named arguments
def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f"For {k} we have {v}")


pretty_print(username='dang', role='admin')
pretty_print(**{"username": 'dang', "role": 'admin'})
