

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.poziom_szczescia = 0
        self.poprzedni_dystans = 0
        self.suma_dystansow = 0

    def przedtaw_sie(self):
        return(f"Jestem {self.imie} {self.nazwisko}")

    def zrob_przebiezke(self, dystans):
        if self.poprzedni_dystans is not None and dystans > self.poprzedni_dystans:
            self.poziom_szczescia += 1
        self.poprzedni_dystans = dystans

        ile_pelnych_dziesiatek_popprzednio = self.suma_dystansow // 10
        self.suma_dystansow += dystans
        ile_pelnych_dziesiatek_teraz = self.suma_dystansow // 10
        ile_nowych_dziesitaek = ile_pelnych_dziesiatek_teraz - ile_pelnych_dziesiatek_popprzednio
        if ile_nowych_dziesitaek > 0:
            self.poziom_szczescia += 3*ile_nowych_dziesitaek

