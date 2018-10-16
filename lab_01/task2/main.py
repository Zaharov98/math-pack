
import common.input


def get_user_advice(user_age):
    if 0 < user_age <= 6:
        return 'Kindergarten'
    elif 6 < user_age <= 18:
        return 'School'
    elif 18 < user_age <= 25:
        return 'University'
    elif 25 < user_age <= 60:
        return 'Work'
    elif 60 < user_age <= 120:
        return 'Have a choose'
    else:
        return 'This program is for people! ' * 5


def main():
    print('\nXXI sanctuary society')

    while True:
        user_age = common.input.input_number(int, 'Input your age: ')
        user_advice = get_user_advice(user_age)

        print(user_advice)


if __name__ == '__main__':
    main()
