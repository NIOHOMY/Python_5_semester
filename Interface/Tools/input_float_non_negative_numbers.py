
def input_float_non_negative_numbers(input_string = "Введите вещественное число >= 0: "):
    user_input = input(input_string)
    
    try:
        number = float(user_input)
        if number >= 0:
            return number
        else:
            return None
    except ValueError:
        return None
