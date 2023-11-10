def check_and_print_binary_multiple_of_3(lines, c1):
    i = 0

    decimal_number = 0
    length = len(line)

    while i < length:
        s_int = ''  # строка для нового числа
        while (i < length) and ('0' <= line[i] <= '1'):
            s_int += line[i]
            i += 1
        i += 1

        if s_int != '':
            decimal_number = int(s_int, 2)
            if decimal_number % 3 == 0:
                c1 += 1
    return c1


# Пользовательский ввод
n = int(input("Введите количество строк: "))
user_lines = []

c = 0
for _ in range(n):
    line = input("Введите строку: ")
    user_lines.append(line)
    c = check_and_print_binary_multiple_of_3(user_lines, c)
    if c != 0:
        print(f"Найдено число в двоичной записи, кратное 3, в строке: {line}")
    else:
        print(f"Чисел в двоичной записи, кратных 3, в строке: {line} не найдено")