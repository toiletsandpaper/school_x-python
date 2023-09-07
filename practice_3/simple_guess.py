# ввод: любое натуральное цисло
# вывод: корень этого числа, если 
# он целый
# если такого корня нет - "трудно, 
# не могу"

# def guess(num: int) -> int | str:

# 81
# 9

# 80
# трудно


def prod_N(x: float, N: int = 3) -> float:
    return float(x * N)

x = float(input())
answer = prod_N(x, 2)
print(answer)