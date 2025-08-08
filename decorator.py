# How to define a decorator in Python
# Usefull when i need to avoid code duplication for example do this capitalizing in a lot of functions

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(args[0].capitalize())
        print("After calling the function")
        return result
    return wrapper

@decorator_func
def print_hello(name: str):
    print("Hello, World! " + name)

if __name__ == "__main__":
    print_hello("vale")