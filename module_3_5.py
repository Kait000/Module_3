def get_multiplied_digits(number):
    if len(str(number)) <= 1:
        if number == 0:  # если последнее число = 0, возвращаем 1 для успешного умножения
            return 1
        return number
    else:
        str_number = str(number)
        first = int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))
        return first


print(get_multiplied_digits(40203))
