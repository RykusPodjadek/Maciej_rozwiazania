
# Zadanie

# Zmienna dane zawiera 24 odczyty temperatury z 24 godzin
# Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza,
# tzn "2150" to 21.50°C
# Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00

# Wypisz do konsoli raport w formacie:
# <godzina>:<tabulator><stopnie z dokładnością do drugiego miejsca po przecinku><znak stopni>C

# Dla odczytów niższych niż lub równych 20°C dodaj "<tabulator>!"
# Dla odczytów niższych niż lub równych 18,5°C dodaj dodatkowy wykrzyknik

# Nie kopiuj proszę znaku stopni. Spróbuj użyć znaku unicode \u00b0

# Docelowy rezultat znajduje się poniżej

# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
#
#
# """
# 00:00:	21.50°C
# 01:00:	21.48°C
# 02:00:	21.20°C
# 03:00:	21.19°C
# 04:00:	21.00°C
# 05:00:	20.76°C
# 06:00:	20.76°C
# 07:00:	20.50°C
# 08:00:	20.65°C
# 09:00:	20.20°C
# 10:00:	20.15°C
# 11:00:	20.10°C
# 12:00:	20.05°C
# 13:00:	20.00°C	!
# 14:00:	20.01°C
# 15:00:	19.93°C	!
# 16:00:	19.90°C	!
# 17:00:	19.50°C	!
# 18:00:	18.34°C	!!
# 19:00:	17.50°C	!!
# 20:00:	17.44°C	!!
# 21:00:	18.60°C	!
# 22:00:	19.46°C	!
# 23:00:	20.10°C
# """

dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
dlugosc = int(len(dane)/4)
i = 0
godz = 0
print('"""')
# u"\u00B0"
for a in range(0, dlugosc):
    if godz < 10:
        if int(dane[i]) < 2 and int(dane[i+1]) <= 8 and int(dane[i+2]) <= 5:
            print("0" + str(godz) + ":00:    "+ dane[i] + dane[i+1] + "." + dane[i+2] + dane[i+3]+u"\u00B0"+"C  !!")
            i += 4
            godz += 1
        elif int(dane[i]) < 2 or (int(dane[i]) == 2 and int(dane[i+1]) == 0 and int(dane[i+2]) == 0 \
            and int(dane[i+3]) == 0 ):
            print("0" + str(godz) + ":00:    "+ dane[i] + dane[i+1] + "." + dane[i+2] + dane[i+3]+u"\u00B0"+"C  !")
            i += 4
            godz += 1
        else:
            print("0" + str(godz) + ":00:    "+ dane[i] + dane[i+1] + "." + dane[i+2] + dane[i+3]+u"\u00B0"+"C")
            i += 4
            godz += 1
    else:
        if int(dane[i]) < 2 and int(dane[i+1]) <= 8 and int(dane[i+2]) <= 5:
            print(str(godz) + ":00:    "+ dane[i] + dane[i+1] + "." + dane[i+2] + dane[i+3]+u"\u00B0"+"C  !!")
            i += 4
            godz += 1
        elif int(dane[i]) < 2 or (int(dane[i]) == 2 and int(dane[i+1]) == 0 and int(dane[i+2]) == 0 \
            and int(dane[i+3]) == 0 ):
            print(str(godz) + ":00:    "+ dane[i] + dane[i+1] + "." + dane[i+2] + dane[i+3]+u"\u00B0"+"C  !")
            i += 4
            godz += 1
        else:
            print(str(godz) + ":00:    " + dane[i] + dane[i + 1] + "." + dane[i + 2] + dane[i + 3]+u"\u00B0"+"C")
            i += 4
            godz += 1
print('"""')
