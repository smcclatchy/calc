def compute(input_string):
    """Perform simple arithmetic based on string input.
    
    Example: '5 + 7' -> 12
    """
    values = input_string.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    else:
        msg = f"Unknown operator: '{operator}'\n"
        msg += "choose from '+' and '-'."
        raise ValueError(msg)