n: int = int(input('N: '))
array: list = list(range(1, n))
i = 0
should_break: bool = False

while True:
    if array[i] % 123 == 0:
        print(array[i], 'делится')
        if should_break is True:
            break
        else:
            should_break = True
    i += 1      # i = i + 1
    
    
# print(i)
# while n > 0:
#     print(n)
#     n = n - 1
    