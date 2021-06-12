lista_ocen = [2.0]


def dodaj_ocene(ocena):
    # Sprawdzam zakres ocen
    if ocena >= 2.0 and ocena <= 6.0:
        lista_ocen.append(ocena)
        return True
    else:
        return False


if dodaj_ocene(1.0):
    print("Dodano ocenę")
else:
    print("Nie udało się dodać oceny")


    def srednia(lista_ocen):
        suma = sum(lista_ocen)

        return suma / (len(lista_ocen))

dodaj_ocene(4.5)
print(srednia(lista_ocen))
print(lista_ocen)

# Zad. 3
lista_ocen3 = [2.0, 4.0, 3.5, 6.0, 5.5]


def wylicz_srednia(n):
    liczba_ocen = len(lista_ocen3)
    ocena = 0
    for num in range(liczba_ocen - n, liczba_ocen):
        ocena += lista_ocen3[num]
        print(ocena)
    sr = (ocena / (liczba_ocen - (liczba_ocen - n)))
    print(f"Średnia: {sr}")


wylicz_srednia(3)


def wylicz_srednia(n):
    robocza = lista_ocen[len(lista_ocen) - n:len(lista_ocen)]
    return sum(robocza) / len(robocza)


###############
# !/usr/bin/python3.8

class Student:
    def __init__(self, imie, nazwisko, kierunek):
        self.lista_ocen = []
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek_studiow = kierunek

    def dodaj_ocene(self, ocena):
        # Sprawdzam zakres ocen
        if ocena >= 2.0 and ocena <= 6.0:
            self.lista_ocen.append(ocena)
            return True
        else:
            return False

    def wylicz_srednia(self, n):
        robocza = self.lista_ocen[len(self.lista_ocen) - n:len(self.lista_ocen)]
        return sum(robocza) / len(robocza)


adam_nowak = Student("Adam", "Nowak", "Tester")
anna_kowalska = Student('Anna', "Kowalska", "Tester")

print(adam_nowak.lista_ocen)

adam_nowak.dodaj_ocene(5.0)
adam_nowak.dodaj_ocene(5.0)
adam_nowak.dodaj_ocene(3.0)
print("Oceny Adama", adam_nowak.lista_ocen)
print("Średnia ocen Adama ", adam_nowak.wylicz_srednia(3))

print("Oceny Ani", anna_kowalska.lista_ocen)




