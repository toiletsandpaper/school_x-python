from typing import TypeAlias, Any 

alphabet = {
    0: 'AA',
    1: 'A',
    2: [1, 2],
    3: set([1, 1, 2, 3, 3, 4]),
    4: {
        1: 'A',
        2: 3,
        3: {
            'A': 12,
            3: 31
        }
    },
    10: 'Y',
    'Z': 10,
    0.1: 'SDA',
    True: 'sdasd',
    False: 123123,
    None: 'dasdasd',
}


# O_letter = alphabet.get('Z', None)
# if not bool(O_letter):
#     print('NO O')

# for key, value in alphabet.items(): # .keys() .values()
#     print(f'Ключ: {key} Значение: {value}')