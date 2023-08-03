
#  a) Zdefiniuj klasę `Osoba`, której w inicjalizacji będzie nadawane imię i nazwisko, które będą przechowywane w klasie.
#
# b) Zdefiniuj metodę `przedstaw_sie`, która będzie zwracała napis składający się z imienia i nazwiska (użyj profesjonalnego sposobu stworzenia takiego napisu!).
#
# c) Dodaj w klasie pole `poziom_szczescia`, która będzie przechowywała informacje o tym, jak szczęśliwa jest dana osoba. Podczas inicjalizacji osoby, nadawaj temu atrybutowi wartość 0.
#
# d) Dodaj metodę `zrob_przebiezke`, która odzwierciedla przeprowadzenie treningu biegowego i jako argument przyjmuje dystans (w km) jaki osoba ma do przebiegnięcia. Jeżeli osoba przebiegnie więcej niż 1 km, to jej poziom szczęścia wzrasta o 1.
#
# e) Dodaj do klasy informacje o poprzednim biegu w postaci pola `last_run` przechowującego liczbę przebiegniętych przez daną osobę kilometrów podczas ostatniego biegu. Zmodyfikuj metodę `zrob_przebiezke` tak, żeby poziom szczęścia rósł o 1 wtedy, gdy osoba w danym biegu przebiegnie więcej niż w biegu poprzednim
#
# f) Dodaj do klasy informację o tym, ile w sumie przebiegła dana osoba do tej pory. Zmodyfikuje metodę `zrob_przebiezke` tak, aby po każdych kolejny pełnych 10-ciu kilometrach poziom szczęścia rósł dodatkowo o 3.


 # nie wiem dlaczego to nie dziala, xD trzeba zsprawdzic xD i to pociwczyc
from ludzie.osoba import Osoba





 if __name__ == '__main__':

     jas = Osoba(imie="Jan", nazwisko="Kowalski")
     print(jas.przedtaw_sie())
     print(jas.poziom_szczescia)
     jas.zrob_przebiezke(5)
     print(jas.poziom_szczescia)
     jas.zrob_przebiezke(20)
     print(jas.poziom_szczescia)
     jas.zrob_przebiezke(7)
     print(jas.poziom_szczescia)






