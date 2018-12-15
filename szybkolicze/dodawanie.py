import random


def dodawanie(x, y):
    a, b = 0, 0

    x_1 = x % 10  # jedności pierwszej liczby

    print("Ile to będzie %s + %s = ?" % (x, y))
    if x_1 + y > 10:
        a1 = 10 - x_1
        b1 = y - a1

        for i in range(3):
            cyfry = input(
                "    Najpierw napisz na jakie cyfry rozdzielisz %s? (połącz je znakiem +): " % y)
            try:
                a, b = cyfry.split('+')
            except ValueError:
                print("    Nie rozumię. Podaj dwie cyfry połączone +, np.: 3+4")
                continue

            if a1 == int(a) and b1 == int(b):
                print("    Dobrze!")
                break
            else:
                if i >= 1:
                    print("    Niestety nie. Podpowiedź: Ile %s brakuje do pełnej 10?" % str(x_1))
                else:
                    print("    Niestety nie. Spróbuj jeszcze raz!")


if '__main__' == __name__:
    X = random.randint(10, 99)
    Y = random.randint(0, 9)
    dodawanie(X, Y)
