import module 

z = 12

def outer(y):
    print(f'y in outer before assig: {"y" in locals()}')
    y = 12
    print(f'y in outer after assig: {"y" in locals()}')
    def answer(y):
        asdas = 12 + y + z
        print(f'y in answer: {"y" in locals()}')
        print(locals())
        print(globals())
        return asdas
    return answer(y)


if __name__ == '__main__':
    x: int = 42
    print(
        f'y in main is exists: {"y" in locals()}',
    )
    outer(10)
    