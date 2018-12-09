import random


def dodawanie(x, y):
    a, b = 0, 0

    x_1 = x % 10  # jedności pierwszej liczby

    print("%s + %s =" % (x, y))
    if x_1 + y > 10:
        a1 = 10 - x_1
        b1 = y - a1

        for i in range(3):
            cyfry = input("Na jakie cyfry podzielisz %s?  = " % (y))
            try:
                a, b = cyfry.split(' ')
            except ValueError:
                print("Nie rozumię. Podaj dwie cyfry rodzielone spacją")
            # if i > 1:
            #     print("Nie. Podpowiedź: Ile % brakuje do pełnej 10?" % str(x_1))
            if a1 == int(a) and b1 == int(b):
                print("Dobrze!")
                break


if '__main__' == __name__:
    X = random.randint(10, 99)
    Y = random.randint(0, 9)
    dodawanie(X, Y)
