
# Zadanie 1
# Napisz algorytm, który sprawdzi, czy liczba jest parzysta
# BONUS pobierz liczbę od użytkownika


# Zadanie 2
# Poproś użytkownika o login (lub wpisz ręcznie)
# Sprawdź, czy zgadza się z "adamnowak" i wypisz informację
# (Dla loginów nie ma znaczenia wielkość liter)


# Zadanie 3
# Poproś użytkownika "adam" o nowe hasło
# Sprawdź, czy jego login się w nim zawiera
# (wielkimi lub małymi literami) i wypisz informację


# Zadanie 4
# Poproś użytkownika o nowe hasło i sprawdź czy jest bezpieczne, tzn.:
# Ma 8 znaków lub więcej
# Nie zawiera roku 2019, ani miesiąca (obecnego, słownie, czyli "wrzesien", niezależnie od wielkości liter)
# Zawiera przynajmniej jeden znak specjalny "#", "@" lub "#"

nowe_haslo = input("Podaj nowe hasło: ")

if len(nowe_haslo) < 8 :
    print ("To jest zbyt krótkie hasło! Podaj hasło z min 8 znaków")
elif "2019" in nowe_haslo or "wrzesien" in nowe_haslo :
    print ("Hasło nie może zawierać '2019' ani 'wrzesien!")
elif "#" in nowe_haslo :
    print ("OK, to jest bezpieczne hasło!")
elif "$" in nowe_haslo :
    print ("OK, to jest bezpieczne hasło!")
elif "@" in nowe_haslo :
    print ("OK, to jest bezpieczne hasło!")
else: print ("Hasło musi zwierać znak specjalny '#', '@' lub '$'!")


# Zadanie 5
# Poproś użytkownika o fragment tekstu, a następnie o słowo
# Określ na której pozycji rozpoczyna się dane słowo w danym tekscie używając metody find()
# Wypisz odpowiedni komunikat - jedne w przypadku sukcesu, drugi w przypadku porażki (braku słowa w tekscie)
#
# Np.:
# Dla tekstu "Ala ma kota" i słowa "kot"
# "Słowo "kot" znajduje się na 7 pozycji."
#
# Dla tekstu "Ala ma kota" i słowa "pies"
# "Słowo "pies" nie znajduje się w tekscie."

tekst = input("Podaj tekst: ")
slowo = input("Podaj słowo: ")
pozycja = tekst.find(slowo)
if slowo in tekst:
    print ("Słowo " + slowo + " znajduje się na " + str(pozycja) + " pozycji. ")
else:
    print ("Słowo " + slowo + " nie znajduje się w tekście " + tekst + "!!!")

# Zadanie 6
# Rozwiń powyższy program dodając do komunikatu wizualizację:
# Wszystkie elementy tekstu które nie są pierwszym wystąpieniem słowa zamień na "_"
#
# Np.:
# Dla tekstu "Ala ma kota" i słowa "kot"
# "Słowo "kot" znajduje się na 7 pozycji."
# "_______kot_"
#
# Dla tekstu "Ala ma kota" i słowa "pies"
# "Słowo "pies" nie znajduje się w tekscie."
# "___________"
#
# Uwaga! Zależy nam na wizualizacji, a nie wartości - użyj mądrego tworzenia stringa i indeksowania,
# a nie podmiany wartości.


# Zadanie 7
# Pobierz liczbę od użytkownika
# Sprawdź czy użytkownik faktycznie podał liczbę (metoda isdigit() typu string)
# Jeżeli tak to sprawdź podzielność przez kolejno 3, 5 i 7 (nie naraz)
# Wypisz rezultat dla każdego sprawdzenia
# Np. dla liczby 21
# "Liczba 21 jest podzielna przez 3!"
# "Liczba 21 jest podzielna przez 7!"


# Zadanie 8
# Pobierz wynik sprawdzianu od użytkownika
# Sprawdź czy jest to liczba i czy jest z zakresu 0 do 100
# Wypisz ocenę na podstawie progu procentowego
# 5 od 90, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50, 2 dla mniej niż 50


# Zadanie 9
# Sprawdź czy jest wygrana w kółko i krzyżyk
# Wejście to 9 znaków oznaczających stan planszy w kolejnych wierszach - "x", "o", lub puste "-"
# Wypisz czy jest wygrana i czyja
# Sprawdź kilka planszy

plansza_1 = "xoo-xo--x"
plansza_2 = "xooxoo--x"
plansza_3 = "xooxoooxx"
