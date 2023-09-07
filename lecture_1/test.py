first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

answer = round(
    (first * first) / second,
    ndigits=1
)

print(f"В итоге получилось: {answer}")
