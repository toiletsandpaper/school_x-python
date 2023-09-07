# def my_personal_sum( # объявляем функцию
#     x: int | float, # переменная х с типом int или float
#     y: int | float, # переменная y с типом int или float
# ) -> int | float: # функция вернёт int или float
#     return x / y

def my_personal_sum(
    num_list: list
) -> int | float:
    answer = 0
    for num in num_list:
        answer += num
    return answer

# def my_personal_sum(*args, **kwargs) -> int | float:
#     # print(f'Args: {args}')
#     # print(f'KWargs: {kwargs}')
#     answer = 0
#     for num in args:
#         answer += num
#     return answer

_list1: list = [1, 2, 3]
_list2: list = [2, 3, 4]

print(
    my_personal_sum(_list1),
    my_personal_sum(_list2),
)
#print(sum([3, 5, 1]))
