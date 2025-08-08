"""
    reverse a string using list slicing
"""

def reverse_string(string: str) -> str:
    # string[start:stop:step]
    return string[::-1]

if __name__ == "__main__":
    print(reverse_string("Programing language"))