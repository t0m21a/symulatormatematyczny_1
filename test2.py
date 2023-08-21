#==========POCZĄTEK======================================================================================================================
#importowanie potrzebnych bibliotek
import time
import random 
#utworzenie potrzebnych zmiennych
punkty = 0
wypełniacz = 0
czas_wyznaczony = 0
wypełniacz_czas = 0
początek = 0
koniec = 0
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#przywitanie z użytkownikiem i objaśnienie działania programu
print("""Witaj! Oto symulator kartkówki z matematyki.
Gra polega na rozwiązywaniu przez Ciebie przykładów matematycznych.
Będziesz mógł wybrać operację: dodawanie(+), odejmowanie(-), mnożenie(*), dzielenie(/), lub dzielenie całkowite(//),
lub "losowo", czyli każde działanie, z losową operacją. 
Określlisz również liczbę działań jaką chcesz rozwiązać, 
poziom trudności dostępne opcje:
1 - dwie liczby w zakresie 1-10
2 - 1 liczba 10-100 2 liczba 1-10
3 - 1 liczba 100-1000 2 liczba 10-100
Uwaga! W przypadku wyboru operacji "dzielenie", "dzielenie całkowite", lub "losowo" dla ułatwienia możesz wybrać tylko opcję poziomu 1.
Następnie zostaniesz zapytany o pomoiar czasu podczas testu oraz o gotowość (w razie braku gotowości poczekam ile chcesz)
Kolejnym krokiem będzie rozwiązanie przez Ciebie działań z losowo wygenerowanymi liczbami.
Dobra odpowiedź=10 pkt, zła odpowiedź=0 pkt, pomyłka o 1=5 pkt
Następnie jeśli wyrazisz chęć pokażę Twoją ocenę, czas, oraz spytam Cię o wrażenia.
Przeczytaj UWAŻNIE całą instrukcję obsugi programu i wpisuj poprawne dane w opdowiednie pola, aby unikać błędów programu.
Mam nadzieję, że wszystko zrozumiałeś. 
Zaczynamy!""")
#-------------------------------------------------------------------------------------------------------------------------------
#==========Pytania do użytkownika==========
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Pytanie o operację 
while True:
    try:
        odpowiedz_operacja = int(input("""wybierz operację. Wpisz 1,2,3,4, lub 5.
        1. dodawanie
        2. odejmowanie
        3. mnożenie
        4. dzielenie
        5. dzielenie całkowite 
        6.losowo                                                                  
        """))
        if odpowiedz_operacja in [1, 2, 3, 4, 5, 6]:
            break
        else:
            print("""Błedne dane! Wprowadź 1, 2, 3, 4, 5 lub 6.""")
    except ValueError:
        print("""Błedne dane! Wprowadź Wprowadź 1, 2, 3, 4, 5 lub 6.""")
if odpowiedz_operacja in [5]:
    print("Uwaga! Twój wybór to dzielenie całkowite. W związkiu z tym prosze abyś wpisywał tylko liczby całkowite bez ich części po przecinku.")
elif odpowiedz_operacja in [4]:
    print("Uwaga! Twój wybór to dzielenie. Wpisuj zatem liczby wraz z ich częściami po przecinku. Dla ułatwienia możesz wybrać tylko poziom 1.")
elif odpowiedz_operacja in [6]:
    print("Uwaga! Twój wybór to losowo, zatem dla ułatwienia możesz wybrać tylko poziom 1.")
else:
    if odpowiedz_operacja==1:
        odpowiedz_operacja2 = "dodawanie"
    elif odpowiedz_operacja==2:
        odpowiedz_operacja2 = "odejmowanie"
    elif odpowiedz_operacja==3:
        odpowiedz_operacja2 = "mnożenie"
    print("Ustawiam Twój wybór jako:", odpowiedz_operacja2)
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Pytanie o liczbę działań
time.sleep(1)
while True:
    try:
        pytanie_o_działania_1 = float(input("""Ile chcesz rozwiązać działań? Wpisz liczbę w przedziale 1-100 """))
        if 1 <= pytanie_o_działania_1 <= 100:
            break
        elif pytanie_o_działania_1 < 1:
            print("Błędne dane! Liczba musi wynosić minimum 1!")
        elif pytanie_o_działania_1 > 100:
            print("Za duża liczba! Wprowadź liczbę w przedziale 1-100!")

    except ValueError:
        print("Niepoprawna odpowiedź. Wprowadź liczbę.")
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Pytanie o poziom
while True:
    try:
        odpowiedz_poziom = int(input("Wybierz poziom testu. Wprowadź liczbę 1, 2 lub 3: "))
        if  odpowiedz_operacja in [1, 2, 3] and odpowiedz_poziom in [1, 2, 3]:
            break
        elif odpowiedz_operacja in [4, 5, 6] and odpowiedz_poziom in [1]:
            break
        elif odpowiedz_operacja in [4, 5, 6] and odpowiedz_poziom in [2, 3]:
            print("Twój wybór operacji to dzielenie, dzielenie całkowite, lub losowo, więc możesz wybrać tylko poziom 1!")
        else:
            print("Wpisz prawidłowe dane.")
    except ValueError:
        print("Wpisz prawidłowe dane.")
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Pytanie o czas
while True:
    try:
        odpowiedz_pomiar_czasu = str(input("Czy chcesz abym zmierzył Ci czas? Odpowiedz TAK, lub NIE."))
        if odpowiedz_pomiar_czasu in ["TAK", "NIE"]:
            break
        else:
            print("Wprowadź prawidłowe dane!")
    except ValueError:
        print("Wprowadź prawidłowe dane!")
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Pytanie o gotowość
while True:
    try:
        pytanie_1 = input("""Gotowy??? Odpowiedz TAK, lub NIE.""")
        if pytanie_1 in ["TAK", "NIE"]:
            break
        else:
            print("Błędne dane! Wprowadź TAK, lub NIE.")
    except ValueError:
        print("Niepoprawna odpowiedź. Wprowadź TAK, lub NIE.")
if pytanie_1 == "TAK":
    time.sleep(1.5)
    print("Okej, zaczynajmy!")
elif pytanie_1 == "NIE":
    print("Okej, w takim razie chwilę poczekam.")
    while True:
        try:
            czas_wyznaczony = czas_wyznaczony+int(input("Podaj ilość czasu jaką mam odczekać w sekundach."))
            if czas_wyznaczony>=0:
                while czas_wyznaczony!=0:
                    print(czas_wyznaczony)
                    time.sleep(1)
                    czas_wyznaczony=czas_wyznaczony-1
                break
            elif czas_wyznaczony<=-1:
                print("Błędne dane! Wprowadź liczbe większą niż 0 lub równą 0!")
        except ValueError:
            print("Niepoprawna odpowiedź. Wprowadź liczbę.")
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Komunikaty i czekanie
print("Powodzenia!")
time.sleep(0.5)
print("Zaczynamy!")
time.sleep(0.5)
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Działania z czasem
if odpowiedz_pomiar_czasu in ["TAK"]:
    print("Czas start!")
    początek=początek+float(time.time())
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#==========Główna część programu-pętla==========
while wypełniacz <pytanie_o_działania_1:
    #Losowanie liczb
    if odpowiedz_poziom==1:
        Liczba_1 = random.randrange(1, 10)
        Liczba_2 = random.randrange(1, 10)
    elif odpowiedz_poziom==2:
        Liczba_1 = random.randrange(10, 100)
        Liczba_2 = random.randrange(1, 10)
    elif odpowiedz_poziom==3:
        Liczba_1 = random.randrange(100, 1000)
        Liczba_2 = random.randrange(10, 100)
    #Pokazywanie działania
    print("Oto Twoje działanie:")
    if odpowiedz_operacja in [1]:
        print(Liczba_1, "+", Liczba_2)
    elif odpowiedz_operacja in [2]:
        print(Liczba_1, "-", Liczba_2)
    elif odpowiedz_operacja in [3]:
        print(Liczba_1, "*", Liczba_2)
    elif odpowiedz_operacja in [4]:
        print(Liczba_1, "/", Liczba_2)
    elif odpowiedz_operacja in [5]:
        print(Liczba_1, "//", Liczba_2)
    elif odpowiedz_operacja in [6]:
        lista_losowa_operacja = "+", "-", "*", "/", "//"
        losowa_operacja = random.choice(lista_losowa_operacja)
        print(Liczba_1, losowa_operacja, Liczba_2)
    #System odpowiedzi
    while True:
        try:
            odpowiedz_gracza = input("Podaj odpowiedź:")
            odpowiedz_gracza = float(odpowiedz_gracza)
            break
        except ValueError:
            print("Niepoprawna odpowiedź. Wprowadź liczbę.")
    #Wyznaczanie poprawnej odpowiedzi
    if odpowiedz_operacja in [1]:
        odpowiedz_prawidłowa = float(Liczba_1 + Liczba_2)
    elif odpowiedz_operacja in [2]:
        odpowiedz_prawidłowa = float(Liczba_1 - Liczba_2)
    elif odpowiedz_operacja in [3]:
        odpowiedz_prawidłowa = float(Liczba_1 * Liczba_2)
    elif odpowiedz_operacja in [4]:
        odpowiedz_prawidłowa = float(Liczba_1 / Liczba_2)
    elif odpowiedz_operacja in [5]:
        odpowiedz_prawidłowa = float(Liczba_1 // Liczba_2)
    elif odpowiedz_operacja in [6]:
        if losowa_operacja in ["+"]:
            odpowiedz_prawidłowa = float(Liczba_1 + Liczba_2)
        elif losowa_operacja in ["-"]:
            odpowiedz_prawidłowa = float(Liczba_1 - Liczba_2)
        elif losowa_operacja in ["*"]:
            odpowiedz_prawidłowa = float(Liczba_1 * Liczba_2)
        elif losowa_operacja in ["/"]:
            odpowiedz_prawidłowa = float(Liczba_1 / Liczba_2)
        elif losowa_operacja in ["//"]:
            odpowiedz_prawidłowa = float(Liczba_1 // Liczba_2)
    #System punktacji
    if odpowiedz_gracza == odpowiedz_prawidłowa:
        print("Brawo! Twoja odpowiedź jest prawidłowa! Otrzymujesz 10 punktów :) ")
        punkty=punkty+10
    elif odpowiedz_gracza+1==odpowiedz_prawidłowa or odpowiedz_gracza-1==odpowiedz_prawidłowa:
        print("Było blisko pomyliłeś się o 1, ale otrzymujesz 5 punktów. Prawidłowa odpowiedź to:", odpowiedz_prawidłowa)
        punkty=punkty+5
    elif odpowiedz_prawidłowa!=odpowiedz_gracza:
        print("Niestety, Twoja odpowiedź jest zła. Otrzymujesz 0 punktów :(. Prawidłowa odpowiedź to: ", odpowiedz_prawidłowa)
    
    wypełniacz = wypełniacz+1
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Działania z czasem
if odpowiedz_pomiar_czasu=="TAK":
    koniec=koniec+float(time.time())
    print("Czas stop!")
elif odpowiedz_pomiar_czasu=="NIE":
    wypełniacz_czas = 1
czas_użytkownika=float(koniec-początek)
time.sleep(2)
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Obliczanie procent z punktów
pytanie_o_działania_1 = pytanie_o_działania_1*10
punkty_2 = punkty/pytanie_o_działania_1
punkty_2 = punkty_2*100
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#==========Skala ocen==========
if punkty_2 >= 0 and punkty_2 <= 20:
    ocena = "Niedostateczny(1)"
elif punkty_2 >= 21 and punkty_2 <= 40:
    ocena = "Dopuszczający(2)"
elif punkty_2 >= 41 and punkty_2 <= 70:
    ocena = "Dostateczny(3)"
elif punkty_2 >= 71 and punkty_2 <= 80:
    ocena = "Dobry(4)"
elif punkty_2 >= 81 and punkty_2 <= 90:
    ocena = "Bardzo dobry(5)"
elif punkty_2 >= 91 and punkty_2 <= 100:
    ocena = "Celujący(6)"
else:
    ocena = "Niepoprawna ilość punktów"
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#Komunikaty do użytkownika
print("Koniec. Rozwiązałeś już działania.")
time.sleep(1.5)
print("Oto liczba zdobytych przez Ciebie punktów w procentach:", punkty_2, "%")
time.sleep(1.5)
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#==========Pytania do użytkownika==========
#Pytanie o pomiar czasu
if odpowiedz_pomiar_czasu=="TAK":
    while True:
        try:
            odpowiedz_pomiar_czasu_2 = str(input("Czy chcesz poznać swój czas? Wpisz TAK, lub NIE."))
            if odpowiedz_pomiar_czasu_2 in ["TAK"]:
                print("Oto Twój czas:", czas_użytkownika)
                break
            elif odpowiedz_pomiar_czasu_2 in ["NIE"]:
                print("Okej")
            else:
                print("Błędne dane!")
        except ValueError:
            print("Błędne dane!")
elif odpowiedz_pomiar_czasu=="NIE":
    wypełniacz_czas = 1
time.sleep(0.5)
#Pytanie o ocenę
while True:
    try:
        odpowiedz_co_do_oceny = input("Czy chcesz poznać swoją ocenę??? Odpowiedz TAK, lub NIE")
        if odpowiedz_co_do_oceny in ["TAK", "NIE"]:
            break
        else:
            print("Nie rozumiem. Wpisz poprawne dane.")
    except ValueError:
        print("Nie rozumiem. Wpisz poprawne dane.")
if odpowiedz_co_do_oceny=="TAK":
    print("Oto Twoja ocena:", ocena)
else:
    print("Okej")

#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
time.sleep(0.75)
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
#==========Pytania do użytkownika==========
#Pytanie o odczucia
while True:
    try:
        odczucia_użytkownika = str(input("Powiedz mi jeszcze czy Ci się podobało odpowiedz TAK lub NIE"))
        if odczucia_użytkownika in ["TAK", "NIE"]:
            break
        else:
            print("Błędne dane!")
    except ValueError:
        print("Błędne dane!")
if odczucia_użytkownika=="TAK":
    print("Super!")
else:
    print("""Szkoda.Czy jest coś co możemy poprawić? Wybierz numer 1-4.
        1. Język
        2. Mechanika
        3. Działanie symulatora
        4. Inne błędy, lub niedogodności
        5. Nic """)
        
    while True:
        try:
            odpowiedz_odp1 = float(input("Podaj odpowiedź"))
            if odpowiedz_odp1 in[1, 2, 3, 4, 5]: 
                print("Okej, postaram się to poprawić.")   
                break
            else:
                print("Błędne dane!")
        except ValueError:
            print("Błędne dane!")
print("Żegnaj")
#==========KONIEC=========================================================================================================================




  


























