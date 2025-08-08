import re

if __name__ == "__main__":
    a = 'Python is 1'
    characters = re.sub("[a-zA-z]", "", a)
    print(characters) 