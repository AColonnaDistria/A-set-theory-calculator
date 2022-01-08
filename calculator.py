def zero():
    return []
def succ(n):
    return [zero(), n]
def pred(n):
    if n == zero():
        return None
    return n[1]

def eq(n, m):
    if n == zero() or m == zero():
        return m == zero()
    return eq(pred(n), pred(m))

def add(n, m):
    if n == zero():
        return m
    if m == zero():
        return n
    return add(pred(n), succ(m))

def prod(n, m):
    if m == zero():
        return zero()
    return add(prod(n, pred(m)), n)

def convert_int_set(number):
    if number == 0:
        return zero()
    return succ(convert_int_set(number - 1))

def convert_set_int(setValue):
    if setValue == zero():
        return 0
    return 1 + convert_set_int(pred(setValue))

while True:
    print("Number 1 :")
    n = int(input())
    print("Number 2 :")
    m = int(input())

    a = convert_int_set(n)
    b = convert_int_set(m)

    c = add(a, b)
    S = convert_set_int(c)
    print(n,'+',m,'=',S)

    d = prod(a, b)
    P = convert_set_int(d)
    print(n,'x',m,'=',P)
