"""
    Validate if a string has valid parenthesis
    Ex:
        ()[]{} True
        (())[]{} True
        (([])) True
        ({])[]{} False
        {] wrong False
        ( False
    assumption:
        - Only valid characters will be sent (), {} and []
"""
import pdb
def validate_parentheses(string: str)-> bool:
    if len(string) == 1:
        return False
    validate = {"(": ")", "[":"]", "{":"}"}
    stack = []
    for i, ch in enumerate(string):
        if ch in validate: # Caracter de abrir
            stack.append(ch)
        elif validate[stack[-1]] == ch:
            stack.pop()
            continue
        else:
            return False
    return True

if __name__ == "__main__":
    print(validate_parentheses("()[]{}"))
    print(validate_parentheses("{]"))
    print(validate_parentheses("("))
    print(validate_parentheses("(([]))"))
    print(validate_parentheses("({])[]{}"))

    # Easy si es caracter de apertura lo sumo al stack
    # si es caracter de cierre miro el ultimo en el stack sea igual a la key en validate para ese ch de cierre
    # si lo es pop ese ultimo item y continuo
    # si no lo es return false