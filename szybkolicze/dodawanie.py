import random


def dodawanie(x, y):
    a, b = 0, 0

    x_1 = x % 10  # jedności pierwszej liczby

    if x_1 + y <= 10:
        for i in range(3):
            wynik = input("Ile to będzie %s + %s = " % (x, y))
            if int(wynik) == x + y:
                print("    Dobrze!")
                return True
            else:
                print("    Niestety nie. Spróbuj jeszcze raz!")
        print("    Niestety nie udało się :(. %d + %d = %d" % (x, y, x + y))
    else:
        print("Ile to będzie %s + %s = ?" % (x, y))
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
                for _ in range(3):
                    wynik = input("    To ile to będzie %d + %d = %d + %d + %d = " % (x, y, x, a1, b1))
                    if int(wynik) == x + y:
                        print("    Dobrze!")
                        return True
                    else:
                        print("    Niestety nie. Spróbuj jeszcze raz!")
                print("    Niestety nie udało się :(. %d + %d = %d" % (x, y, x + y))

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
