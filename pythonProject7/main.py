import re

def find_binary_multiple_of_3(lines):
    pattern = re.compile(r'^0*(1(01*0)*1|0*)*$')  # Регулярное выражение для чисел, кратных 3 в двоичной системе

    for line in lines:
        if pattern.match(line):
            print(f"Найдено число в двоичной записи, кратное 3: {line}")

# Пример использования
n = int(input("Введите количество строк: "))
user_lines = []

for _ in range(n):
    line = input("Введите строку: ")
    user_lines.append(line)
find_binary_multiple_of_3(user_lines)
