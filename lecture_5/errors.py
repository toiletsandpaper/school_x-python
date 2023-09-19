def convert_ab_to_int(a: str, b: str) -> tuple[int, int]:
    a, b = int(a), int(b)
    return a, b


def divide_ab(a: int | float, b: int | float) -> float:
    #raise IndentationError('dasdsad')
    if 3 in [a, b]:
        raise AttributeError('Я НЕНАВИЖУ ТРОЙКИ')
    return a / b

while True:
    a, b = input('Введите два числа для их суммы: ').split()
    division_score = None
    try:
        a, b = convert_ab_to_int(a, b)
        division_score = divide_ab(a, b)
    except (ZeroDivisionError, ValueError) as e:
        print(f'Ошибка: {e}')
        print('Дружище, ты дурак, введи числа!! И без нулей пж!!')
        print()
        continue
    except AttributeError as ex:
        print(f'Разработчик злой писюкан, потому что он, цитата "{ex}"')
        print('сделай пж как он просит')
        break
    except Exception as ex:
        print(f'Че-то новенькое: {ex}')
    finally:
        print('мы в финале шоу танцы')
    
    
    
    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print(f'{a} / {b} = {division_score}')
    print()