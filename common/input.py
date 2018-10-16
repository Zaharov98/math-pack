
def input_number(number_type, prompt, error='Invalid input'):
    while True:  # input without error
        try:
            number = number_type(input(prompt))
        except ValueError:
            print(error)
        except Exception as e:
            print(e)
        else:
            break
    return number