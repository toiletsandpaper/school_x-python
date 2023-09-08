i: int = 0
f: float = .0
s: str = 'sdads'
b: bool = True
n: None = None

_list1: list = [1, 3, 23, 45, 0, None, 'sad', False]
_list2: list = [i, f, s, b, n]

_set1: set = set([i, f, s, b, n])
_set2: set = {i, f, s, b, n}
_set3: set = {
    'm', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i'
}

_set4: set = {
    'm', 'a', 'm', 'a'
}
_set4_list = list(_set4)
print(_set4)
print(_set4)
print(_set4_list[0])
#print(_set3.intersection(_set4))