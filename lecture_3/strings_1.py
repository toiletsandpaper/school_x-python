import string

# new_name: str = input('type name: ')
# # greet_message: str = 'hello bob'
# # greet_message: str = (
# #     greet_message[:-3] + new_name
# # )
# # greet_message: str = \
# #     greet_message.replace(' bob', f' {new_name}')
# print(greet_message)


# words: str = '<!---dsa das das---!>'

# print(
#    words.strip('<!>-').split()
# )


numbers: str = string.digits
word: str = 'hell123o b32ob ho312w ar3e y231ou'
# for number in numbers:
#     word = word.replace(number, '')
# _word: str = ''
# _sum: float = 0.0
# _prod: float = 1.0
# _list: list = []
# _set: set = set([])
# _dict: dict = {}

# for ch in word:
#     if ch in numbers:
#         continue
#     else:
#         _word += ch
# word = _word
# del _word
        

# print(
#     word
# )


# words: str = 'Hello Bob, are you a bob? BOB!!!'
# #words = words.lower().find('bob')

# while True:
#     bob_index = words.lower().find('bob')
#     if bob_index == -1:
#         break
#     else:
#         words = (
#             words[:bob_index] +
#             'Gregory' +
#             words[bob_index+len('bob'):]
#         )
#         #words = words.lower().replace('bob', 'gregory')
#         print(words, len('bob'))

# print(
#     words
# )


_list: list = [1, 2, 3]
_str: str = '123'
_tuple: tuple = (
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
)

# 3 -> 5

_list[-1] = 5
_tuple[1][1] = 5

print(_list, _str, _tuple)