def get_digit_number(n: int):
    if n == 0: return 1
    digit_number = 0
    while n != 0:
        n = n // 10
        digit_number += 1
    return digit_number


while True:
    try:
        N = int(input("Введите число N: "))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Неверный формат числа, попробуйте снова.')
i = 0
n = 0
while True:
    if n == N:
        break
    if i % get_digit_number(i) == 0:
        print(i, end=' ')
        n += 1
    i += 1
