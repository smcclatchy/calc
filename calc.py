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
    else:
        raise ValueError('Unknown operator!')