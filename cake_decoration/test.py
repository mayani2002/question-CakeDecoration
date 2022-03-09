import random as rnd


def test00():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(1, 20000)
        print(n)

        for _ in range(n):
            l = rnd.randint(1, 100000)

            print(l, end=" ")
        print()

def test01():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(20001, 40000)
        print(n)

        for _ in range(n):
            l = rnd.randint(1, 100000)

            print(l, end=" ")
        print()

def test02():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(40001, 60000)
        print(n)

        for _ in range(n):
            l = rnd.randint(1, 100000)

            print(l, end=" ")
        print()

def test03():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(60001, 80000)
        print(n)

        for _ in range(n):
            l = rnd.randint(1, 100000)

            print(l, end=" ")
        print()

def test04():
    t = 20

    print(t)
    for _ in range(t):
        n = rnd.randint(80001, 100000)
        print(n)

        for _ in range(n):
            l = rnd.randint(1, 100000)

            print(l, end=" ")
        print()

test00()