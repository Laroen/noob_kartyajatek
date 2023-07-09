import random
import time
import magyar
import pandas
import numpy

kartya_szinek = ['pikk', 'kör', 'káró', 'treff']
kartya_ertekek = ['2','3','4','5','6','7','8','9','10','J','D','K','A']

def fo_menu():
    print('1 - új asztal megnyitása:')
    print('2 - új játékos felvétele:')
    print('3 - új játék indítása:')
    print('4 - Nyitott asztal adatai:')
    print('0 - Bezárás:\n')
    valaszt = input('Adja meg a menüpontot: ')
    return valaszt

def menu_1():
    asztal = []
    asztal.append(f'{random.choice(magyar.vezeteknev)}'+' '+f'{random.choice(magyar.keresztnev_v)}')
    asztal.append(input('Hány hely van az asztalnál: '))
    asztal.append(int(input('Mennyi a belépési limit az asztalhoz: ')))
    return asztal

def menu_2():
    nev_1 = f'{random.choice(magyar.vezeteknev)}'+' '+f'{random.choice(magyar.keresztnev_v)}'
    jatekosok.append(Jatekos(nev_1))



def menu_3(data):
    if data == None:
        print('Sajnos a játék nem indítható, még nincs asztal nyitva!')
    elif data.szekek_szama <=1:
        print('2-nél kevesebben ülnek az asztalnál így nem lehet játékot indítani!')
    else:
        print('Játék elindítva\n')


def menu_4(a):
    if a == None:
        print('Sajnos még nincs nyitott asztal!')
    else:
        print(a)

def leosztas(table,players):
    i_ndex = 1
    tet_ossz = 0
    while i_ndex != 4:
        akt_tet = 0
        print(f'{i_ndex}. leosztás')
        for i_szek in range(table.szekek_szama):
            if players[i_szek].jatszik:
                if akt_tet <= players[i_szek].tokens:
                    if i_ndex > 1:
                        print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                        emel_valasz = input(f'{players[i_szek].nev}: tartja, emel, vagy kiszáll (t/e/k) : ')
                        if i_szek == 0 and emel_valasz == 't':
                            continue
                        elif emel_valasz == 'e':
                            if players[i_szek].szek == 1:
                                my_tet = int(input(f'{players[i_szek].nev} tegye meg tétjét: '))
                                players[i_szek].tet = my_tet
                                akt_tet = my_tet
                                players[i_szek].tokens -= players[i_szek].tet
                                players[i_szek].token_veszteseg += players[i_szek].tet
                                tet_ossz += players[i_szek].tet
                                print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                            else:
                                my_tet = int(input(f'{players[i_szek].nev} tegye meg tétjét: '))
                                players[i_szek].tet = akt_tet + my_tet
                                players[i_szek].tokens -= players[i_szek].tet
                                players[i_szek].token_veszteseg += players[i_szek].tet
                                tet_ossz += players[i_szek].tet
                                print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                                if akt_tet == 0:
                                    for i in players:
                                        if i.jatszik and i.tet == 0 and i.szek < players[i_szek].szek:
                                            print(f'{i.nev} Tokenjei: {i.tokens}')
                                            emel_valasz = input(f'{i.nev}: tartja, vagy kiszáll (t/k) : ')
                                            if emel_valasz == 't':
                                                i.tet = players[i_szek]
                                                i.tokens -= players[i_szek].tet
                                                i.token_veszteseg += players[i_szek].tet
                                                tet_ossz += i.tet
                                            elif emel_valasz == 'k':
                                                i.jatszik = False
                                                i.lapok = []
                                akt_tet += my_tet
                        elif emel_valasz == 'k':
                            players[i_szek].jatszik = False
                            players[i_szek].lapok = []
                        else:
                            players[i_szek].tet = akt_tet
                            players[i_szek].tokens -= players[i_szek].tet
                            players[i_szek].token_veszteseg += players[i_szek].tet
                            tet_ossz += players[i_szek].tet
                            print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                    else:
                        if players[i_szek].szek < 2:
                            print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                            my_tet = int(input(f'{players[i_szek].nev} tegye meg tétjét: '))
                            players[i_szek].tet = my_tet
                            akt_tet = my_tet
                            players[i_szek].tokens -= players[i_szek].tet
                            players[i_szek].token_veszteseg += players[i_szek].tet
                            tet_ossz += players[i_szek].tet
                        else:
                            print(f'{players[i_szek].nev} Tokenjei: {players[i_szek].tokens}')
                            emel_valasz = input(f'{players[i_szek].nev}: tartja, vagy kiszáll (t/k) : ')
                            if emel_valasz == 't':
                                players[i_szek].tet = akt_tet
                                players[i_szek].tokens -= players[i_szek].tet
                                players[i_szek].token_veszteseg += players[i_szek].tet
                                tet_ossz += players[i_szek].tet
                            elif emel_valasz == 'k':
                                players[i_szek].jatszik = False
                                players[i_szek].lapok = []
                else:
                    players[i_szek].jatszik = False
                    print('Nincs elég tokened erre a körre')
                players[i_szek].tet = 0
            else:
                continue
        if i_ndex != 3:
            huzott_lap = table.pakli[-1]
            asztalon_kartyak.append(huzott_lap)
            kivett_lapok.append(huzott_lap)
            table.pakli.remove(huzott_lap)
            '''print(f'1.: {players[0].lapok[0].__str__},'
                  f' {players[0].lapok[1].__str__}'
                  f' 2.: {players[1].lapok[0].__str__},'
                  f' {players[1].lapok[1].__str__}'
                  f'3.: {players[2].lapok[1].__str__},'
                  f' {players[2].lapok[1].__str__}')'''
            for i in players:
                if i.jatszik:
                    print(f'{i.nev}: {i.lapok[0]}; {i.lapok[1]}  Tokenjei: {i.tokens}')
            print('\nAsztal: ',*asztalon_kartyak, sep='; ')
            time.sleep(15)
            i_ndex += 1
        else:
            for i_vege in players:
                if i_vege.jatszik:
                    print(f'{i_vege.nev}: {i_vege.lapok[0]}, {i_vege.lapok[1]} Token: {i_vege.tokens} - '
                          f'Szék: {i_vege.szek} ')
            print('Asztal: ', *asztalon_kartyak, sep='; ')
            time.sleep(10)
            nyertes = int(input('Melyik széken ülő nyerte meg a kört: '))
            for i_bef in players:
                if i_bef.szek == nyertes:
                    i_bef.tokens += tet_ossz
                    i_bef.token_veszteseg = 0
                    i_bef.tet = 0
                    i_bef.jatszik = False
                    print(f'Gratulálunk {i_bef.nev}-nek A nyereménye: {tet_ossz} Amennyit átvisz a köv leosztásra: '
                          f'{i_bef.tokens}')
            if table.szekek_szama > 0:
                table.szekek_szama = 0
            i_ndex += 1
    return table, players

class Jatekos:
    def __init__(self, nev, tokens=0, tet=0, token_veszteseg=0, jatszik=False, szek=0):
        self.nev = nev
        self.tokens = tokens
        self.tet = tet
        self.token_veszteseg = token_veszteseg
        self.jatszik = jatszik
        self.szek = szek
        self.lapok = []

    def __str__(self):
        return f'{self.nev}: Token: {self.tokens} Lapok: {self.lapok}'


class Kartya:
    def __init__(self,szin_nev,ertek):
        self.szin_nev = szin_nev
        if self.szin_nev == 'pikk':
            self.forma = '♠'
        elif self.szin_nev == 'kör':
            self.forma = '♥'
        elif self.szin_nev == 'káró':
            self.forma = '♦'
        elif self.szin_nev == 'treff':
            self.forma = '♣'
        self.ertek = ertek

    def __str__(self):
        return f'{self.forma}{self.ertek}'


class Asztal:
    def __init__(self, oszto_neve, szekek_szama, belepesi_limit):
        self.oszto_neve = oszto_neve
        self.szekek_szama = int(szekek_szama)
        self.belepesi_limit = int(belepesi_limit)
        self.pakli = []
        for k_sz in kartya_szinek:
            for k_e in kartya_ertekek:
                teszt_kartya = Kartya(k_sz, k_e)
                self.pakli.append(teszt_kartya)

    def __str__(self):
        return f'Osztó neve: {self.oszto_neve}\n' \
               f'Székek száma: {self.szekek_szama} - Belépési limit: {self.belepesi_limit} token'

my_asztal = None
jatekosok = []


while True:
    valaszt_fomenu = fo_menu()
    match valaszt_fomenu:
        case '1':
           my_asztal = Asztal(*menu_1())
        case '2':
            menu_2()
        case '3':
            menu_3(my_asztal)
            index = 1
            asztal_jatekosok = []
            if len(jatekosok) < my_asztal.szekek_szama:
                my_asztal.szekek_szama = len(jatekosok)
            while len(asztal_jatekosok) != my_asztal.szekek_szama:
                tolt = random.choice(jatekosok)
                jatekosok.remove(tolt)
                tolt.tokens = my_asztal.belepesi_limit
                tolt.jatszik = True
                tolt.szek = index
                asztal_jatekosok.append(tolt)
                index += 1
            #print('Az asztalnál ülők száma: ', len(asztal_jatekosok))
            #print('A résztvevő játékosok:', *asztal_jatekosok, sep='\n')  # ide kell majd egy képernyő tisztitas
            while my_asztal.szekek_szama != 0:
                kivett_lapok = []
                for i in range(3):
                    random.shuffle(my_asztal.pakli)
                print(f'\n{my_asztal.oszto_neve} kiosztja a lapokat:')
                for i in range(2):
                    for adat_jatekos in asztal_jatekosok:
                        huzott_lap = my_asztal.pakli[-1]
                        adat_jatekos.lapok.append(huzott_lap)
                        kivett_lapok.append(huzott_lap)
                        my_asztal.pakli.remove(huzott_lap)
                asztalon_kartyak = []
                for i in range(3):
                    huzott_lap = my_asztal.pakli[-1]
                    asztalon_kartyak.append(huzott_lap)
                    kivett_lapok.append(huzott_lap)
                    my_asztal.pakli.remove(huzott_lap)

                for i in asztal_jatekosok:
                    for data in asztalon_kartyak:
                        i.lapok.append(data)
                    print(f'{i.nev}: Token: {i.tokens} Lapok: {i.lapok[0]};{i.lapok[1]}')
                '''df = pandas.DataFrame(vars(i) for i in asztal_jatekosok)
                df.set_index('nev', inplace=True)'''
                print()
                '''for i in df['lapok']:
                    i.append(asztalon_kartyak[0].__str__())
                print(df)'''
                print('Az asztalon lévő kártyák: ',*asztalon_kartyak)
                time.sleep(10)
                while my_asztal.szekek_szama != 0:
                    my_asztal, asztal_jatekosok = leosztas(my_asztal,asztal_jatekosok)
                print()
                my_asztal.szekek_szama=0


        case '4':
            menu_4(my_asztal)
        case '0':
            break
