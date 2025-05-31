

def decor(func):
    def wrapper():
        print("Before")
        res = func()
        print("After")
        return res
    return wrapper

@decor
def pprint_hw():
    return "Hello, world!"


res = pprint_hw()
print(res)


def decor_func_with_params(func):
    def wrapper(*args, **kwargs):
        print("Before")
        res = func(*args, **kwargs)
        print("After")
        return res
    return wrapper

@decor_func_with_params
def create_greeting(name):
    print(f"Creating greetings...")
    return f"Hello, {name}!"

res = create_greeting("Alex")
print(res)


def decor_with_params(decor_arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Before = {decor_arg}")
            res = func(*args, **kwargs)
            print(f"After = {decor_arg}")
            return res
        return wrapper
    return decorator


@decor_func_with_params
@decor_with_params("decor_3")
def create_goodbye(name):
    print(f"Creating godbye words...")
    return f"Godbye, {name}!"

res = create_goodbye("Alex")
print(res)