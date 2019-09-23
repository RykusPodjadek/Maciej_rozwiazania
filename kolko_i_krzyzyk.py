print("   ")
print(" <<< KÓŁKO I KRZYŻYK >>> ")
print("   ")
print("   Numeracja pól: ")
print("     1  2  3 ")
print("     4  5  6 ")
print("     7  8  9 ")
print("   ")
print("     -  -  - ")
print("     -  -  - ")
print("     -  -  - ")
print("   ")

a = " - "
b = " - "
c = " - "
d = " - "
e = " - "
f = " - "
g = " - "
h = " - "
i = " - "

wygrana = False

for j in range(1, 10):

    # TURA KRZYŻYK:
    if j % 2 != 0:
        x = input("Gracz 1 - Gdzie postawić 'X'? (Podaj liczbę od 1 do 9): ")
        while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" \
            and x != "9":
            x = input("Błąd! Podaj liczbę od 1 do 9: ")

        # sprawdzenie zajętości pola:
        while x == "1" and a == " X " or x == "1" and a == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "2" and b == " X " or x == "2" and b == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "3" and c == " X " or x == "3" and c == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "4" and d == " X " or x == "4" and d == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "5" and e == " X " or x == "5" and e == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "6" and f == " X " or x == "6" and f == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "7" and g == " X " or x == "7" and g == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "8" and h == " X " or x == "8" and h == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "9" and i == " X " or x == "9" and i == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")

        # warunki sprawdzone, wszystko OK i podstawiamy:
        if x == "1":
            a = " X "
        elif x == "2":
            b = " X "
        elif x == "3":
            c = " X "
        elif x == "4":
            d = " X "
        elif x == "5":
            e = " X "
        elif x == "6":
            f = " X "
        elif x == "7":
            g = " X "
        elif x == "8":
            h = " X "
        elif x == "9":
            i = " X "

        print(" ")
        print("    " + a + b + c)
        print("    " + d + e + f)
        print("    " + g + h + i)
        print(" ")

        # SPRAWDZENIE WYGRANEJ:
        # poziomy
        if a == " X " and b == " X " and c == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        elif d == " X " and e == " X " and f == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        elif g == " X " and h == " X " and i == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        # piony:
        elif a == " X " and d == " X " and g == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        elif b == " X " and e == " X " and h == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        elif c == " X " and f == " X " and i == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        # przekątne:
        elif a == " X " and e == " X " and i == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break
        elif g == " X " and e == " X " and c == " X ":
            print ("Gracz nr 1 - 'X' wygrywa! :-) ")
            wygrana = True
            break

    # TURA KÓŁKO:
    elif j % 2 == 0:
        x = input("Gracz 2 - Gdzie postawić 'O'? (Podaj liczbę od 1 do 9): ")
        while x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" \
                and x != "9":
            x = input("Błąd! Podaj liczbę od 1 do 9: ")

        # sprawdzenie zajętości pola:
        while x == "1" and a == " X " or x == "1" and a == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "2" and b == " X " or x == "2" and b == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "3" and c == " X " or x == "3" and c == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "4" and d == " X " or x == "4" and d == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "5" and e == " X " or x == "5" and e == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "6" and f == " X " or x == "6" and f == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "7" and g == " X " or x == "7" and g == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "8" and h == " X " or x == "8" and h == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")
        while x == "9" and i == " X " or x == "9" and i == " O ":
            x = input("Pole zajęte! Podaj inną liczbę: ")

        # warunki sprawdzone, wszystko OK i podstawiamy:
        if x == "1":
            a = " O "
        elif x == "2":
            b = " O "
        elif x == "3":
            c = " O "
        elif x == "4":
            d = " O "
        elif x == "5":
            e = " O "
        elif x == "6":
            f = " O "
        elif x == "7":
            g = " O "
        elif x == "8":
            h = " O "
        elif x == "9":
            i = " O "

        print(" ")
        print("    " + a + b + c)
        print("    " + d + e + f)
        print("    " + g + h + i)
        print(" ")

        # SPRAWDZENIE WYGRANEJ:
        # poziomy
        if a == " O " and b == " O " and c == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        elif d == " O " and e == " O " and f == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        elif g == " O " and h == " O " and i == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        # piony:
        elif a == " O " and d == " O " and g == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        elif b == " O " and e == " O " and h == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        elif c == " O " and f == " O " and i == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        # przekątne:
        elif a == " O " and e == " O " and i == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break
        elif g == " O " and e == " O " and c == " O ":
            print ("Gracz nr 2 - 'O' wygrywa! :-) ")
            wygrana = True
            break

if not wygrana:
    print(" REMIS !!! :-D ")