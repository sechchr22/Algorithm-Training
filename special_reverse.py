import re

def reverse_function(input_str: str) -> str:
    # spliting string to have it in list
    # Check if its a special character with isalpha()
    # Go through the string list in reverse order
    # If it is an alphabetic character, append it to a new list
    # If it is a special character, save it in a dictionary with the index
    # Order the dictionary by key DESC
    # Insert the special characters back into their original positions
    # join back the reversed string to return it
    if input_str is None or len(input_str) == 0:
        return input_str

    if bool(re.fullmatch(r"[^a-zA-Z0-9]+", input_str)):
        return input_str

    original = list(input_str)
    reversed_list = []
    i = len(original) - 1
    special_characters = {}
    while i >= 0:
        if original[i].isalpha():
            reversed_list.append(original[i])
        else:
            special_characters[i] = original[i]
        i -= 1
    
    #order special_characters list by key DESC
    special_characters = dict(sorted(special_characters.items()))

    for idx, value in special_characters.items():
        reversed_list.insert(idx, value)

    return ''.join(reversed_list)
    
if __name__ == "__main__":
    # Test cases
    print(reverse_function("abcd")) # "dcba"
    print(reverse_function("ab.c")) # "cb.a"
    print(reverse_function("$%ab.c%d")) # "$%dc.b%a"
    print(reverse_function("#$%&")) # "#$%&"