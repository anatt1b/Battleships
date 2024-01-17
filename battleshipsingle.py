from random import randint

kirjaimet_numeroiksi = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}

#LUODAAN PELILAUDAT
def luo_pelilaudat():
    PIILOPÖYTÄ = [[' '] * 9 for x in range(9)]
    PELIPÖYTÄ = [[' '] * 9 for x in range(9)]
    return PIILOPÖYTÄ, PELIPÖYTÄ

#TULOSTETAAN PELILAUTA
def pelilauta(board):
    print('   A  B  C  D  E  F  G  H  I ')
    print(' ----------------------------')
    rivi_numero = 1
    for rivi in board:
        print("%d|%s |" % (rivi_numero, " |".join(rivi)))
        rivi_numero += 1
    print()

# ASETETAAN LAIVAT LAUDALLE         
def laiva(board):
    # RNG lisää 5 laivaa PIILOPÖYDÄLLE
    for laiva in range(5):
        laiva_rivi, laiva_sarake = randint(0,8), randint(0,8)
        # virheen tarkistus onko laivan paikka jo varattu
        # jos elementissä on jo laiva(X) otetaan uusi yritys
        # == tarkistaa onko elementissä jotain = asettaa sinne jotain
        while board[laiva_rivi][laiva_sarake] == 'X':
            laiva_rivi, laiva_sarake = randint(0,8), randint(0,8)
        board[laiva_rivi][laiva_sarake] = 'X'

# AMMUNTA. TOISIN SANOEN TARKASTETAAN ONKO ELEMENTTIIN AMMUTTU JO JA ONKO SIELLÄ LAIVA
def laukaus():
    try:
        # kysytään pelaajalta mihin elementtiin ammutaan. esin rivi ja sitten sarake.
        # tarkistetaan onhan valinnat niille annetuissa rajoissa.
        rivi = input("Anna rivi numero 1-9: ")
        while rivi not in '123456789':
            print("Syötä validi numero!")
            rivi = input("Anna rivi numero 1-9: ")
        sarake = input("Anna sarake kirjain A-I: ").upper()
        while sarake not in 'ABCDEFGHI':
            print("Syötä validi kirjain!")
            sarake = input("Anna sarake kirjain A-I: ").upper()
        # Kun laukaus on ammuttu se halutaan tallentaa, joten palautetaan annettu arvo.
        # Rivi -1, koska halutaan aloittaa numerosta 1 eikä numerosta 0
        return int(rivi)-1, kirjaimet_numeroiksi[sarake]
    except:
        print("VIRHE!")

# TARKISTETAAN TULIKO OSUMA JA TALLENNETAAN TIETO LASKURIIN.
def osumalaskuri(board):
    laskuri = 0
    # käydään lapi rivit laudalla
    for rivi in board:
        # käydään läpi sarakkeet riviltä
        for sarake in rivi:
            #jos sarakkeessa on X laskuri kasvaa yhdellä mikä tarkoittaa osumaa
            if sarake == 'X':
                laskuri += 1
    # palautetaan laskurin arvo
    return laskuri

STARTTI = True

while STARTTI:

    print("\n\n---------------------------------------------------------------")
    print("Tervetuloa pelaamaan laivanupotusta.")
    print("Ohjeet: ")
    print("Sinulla on 10 ammusta aikaa löytää 5 yhden elementin laivaa.")
    print("Osumasta et menetä ammusta.")
    print("---------------------------------------------------------------")
    # alustetaan laudat tyhjiksi
    PIILOPÖYTÄ, PELIPÖYTÄ = luo_pelilaudat()
    # arvotaan laivat piilopöydälle
    laiva(PIILOPÖYTÄ)

    #pelilauta(PIILOPÖYTÄ)
    turns = 10
    while turns > 0:
        print("     \n         LAIVAN UPOTUS")
        print("       *****************")
        #tulostetaan pelilauta
        pelilauta(PELIPÖYTÄ)
        # kysytään mihin elementtiin ammutaan
        rivi, sarake = laukaus()
        # tarkastetaan onko elementti varattu vai ei
        if PELIPÖYTÄ[rivi][sarake] == '-':
            print("\nAMMUIT JO TÄHÄN\n!")
        elif PELIPÖYTÄ[rivi][sarake] == 'X':
            print("\nOlet jo upottanut tämän laivan!")
        elif PIILOPÖYTÄ[rivi][sarake] == 'X':
            print("\n       *****OSUMA*****")
            PELIPÖYTÄ[rivi][sarake] = 'X'
            #turns -= 1
        else:
            print("\nOHI LAUKAUS!")
            PELIPÖYTÄ[rivi][sarake] = '-'
            turns -= 1
        if osumalaskuri(PELIPÖYTÄ) == 5:
            print("\n****HIHIHIHIII VOITIT PELIN!****\n")
            break
        #print(f"Sinulla on {turns} siirtoa jäljellä!")
        if turns == 1:
            print(f"\nSinulla on {turns} siirto jäljellä!")
        elif turns == 0:
            print("HÄVISIT PELIN!\n")
        else:
            print(f"\nSinulla on {turns} siirtoa jäljellä!")

    uusinta = input("Haluatko pelata uudestaan? k = kyllä, e = ei : ")
    if uusinta != 'k':
        STARTTI = False
        print("Lopetetaan peli.")
