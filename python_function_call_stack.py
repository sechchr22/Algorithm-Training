"""
Python works with LIFO (last in first out) principle
for function call stack
"""


def function_1():
    print("function_1 starts")
    function_2()
    print("function_1 end")

def function_2():
    print("function_2 starts")
    function_3()
    print("function_2 end")

def function_3():
    print("function_3 starts")
    print("function_3 end")


if __name__ == "__main__":
    function_1()