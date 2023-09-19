a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]
#     answer = [0, 0, 3, 0, 5]


def mask_list(array: list[int], mask: list[int]) -> list[int]:
    assert type(array) == list
    return [val * mask[i] * .5 for i, val in enumerate(array)]

def test_mask_list():
    print('проверяем тест маск лист')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0], 'маска работает неправильно'


test_mask_list()

answer = mask_list(array=a, mask=b)
print(answer)



# # 1 вариант
# answer_1 = [val * b[i] for i, val in enumerate(a)]
# print(answer_1)

# # 2 вариант
# answer_2 = []
# for i, val in enumerate(a):
#     answer_2.append(val * b[i])
# print(answer_2)
    
# for i, val in enumerate(a):
#     print(f'index = {i}')
#     print(f'value = {val}\n')