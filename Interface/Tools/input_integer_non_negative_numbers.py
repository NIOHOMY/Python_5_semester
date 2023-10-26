
def input_integer_non_negative_numbers(input_string = "Введите число >= 0: "):
    user_input = input(input_string)
    
    try:
        number = int(user_input)
        if number >= 0:
            return number
        else:
            return None
    except ValueError:
        return None
