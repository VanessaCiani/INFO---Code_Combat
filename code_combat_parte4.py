#Nome: Vanessa Ciani
#Partner: Fabio Monaco
#Classe: 3A INFO
#Data: 23/02/2025

import random

def crea_personaggio(classe):
    if classe == "Guerriero":
        vita = random.randint(100, 120)
        energia = random.randint(8, 10)
        difesa = random.randint(4, 8)
        attacco = sum(random.randint(1, 6) for _ in range(2))  #2d6
        abilità = random.randint(1, 6)  #1d6
        return {"classe": "Guerriero", "vita": vita, "energia": energia, "difesa": difesa, "attacco": attacco, "abilita": abilità}
    
    elif classe == "Mago":
        vita = random.randint(70, 90)
        energia = random.randint(14, 18)
        difesa = random.randint(3, 5)
        attacco = random.randint(1, 20)  #1d20
        abilità = random.randint(1, 6)  #1d6
        return {"classe": "Mago", "vita": vita, "energia": energia, "difesa": difesa, "attacco": attacco, "abilita": abilità}
    
    elif classe == "Ladro":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(3, 5)
        attacco = sum(random.randint(1, 4) for _ in range(3))  #3d4
        abilità = random.randint(1, 4)  #1d4
        return {"classe": "Ladro", "vita": vita, "energia": energia, "difesa": difesa, "attacco": attacco, "abilita": abilità}
    
    elif classe == "Chierico":
        vita = random.randint(80, 100)
        energia = random.randint(10, 12)
        difesa = random.randint(4, 6)
        attacco = random.randint(1, 12)  #1d12
        abilità = random.randint(1, 6)  #1d6
        return {"classe": "Chierico", "vita": vita, "energia": energia, "difesa": difesa, "attacco": attacco, "abilita": abilità}

# Funzione per l'attacco
def attacca(attaccante, difensore):
    if attaccante["energia"] >= 2:
        danno = attaccante["attacco"] - difensore["difesa"]
        if danno > 0:
            difensore["vita"] -= danno
        attaccante["energia"] -= 2
        print(f"{attaccante['classe']} attacca {difensore['classe']} causando {danno} danno.")
    else:
        print(f"{attaccante['classe']} non ha abbastanza energia per attaccare e si riposa.")
        attaccante["energia"] = 10  #Energia ripristinata al massimo

#Funzione per attivare l'abilità speciale del Guerriero
def abilità_berserk(guerriero):
    dado = random.randint(1, 6)
    if dado >= 5:
        #Guerriero fa un altro attacco
        print(f"{guerriero['classe']} lancia Berserk! Fa un altro attacco.")
        return True
    elif dado >= 3:
        #Guerriero fa un altro attacco e perde il 20% della vita
        guerriero["vita"] -= int(guerriero["vita"] * 0.2)
        print(f"{guerriero['classe']} lancia Berserk! Fa un altro attacco ma perde il 20% della sua vita.")
        return True
    else:
        #Guerriero perde il 20% della vita senza attaccare
        guerriero["vita"] -= int(guerriero["vita"] * 0.2)
        print(f"{guerriero['classe']} lancia Berserk! Perde il 20% della sua vita.")
        return False

#Funzione per l'abilità del Mago
def abilità_concentrazione(mago):
    dado = random.randint(1, 6)
    if dado >= 5:
        mago["attacco"] += random.randint(1, 4)  #Aggiunge 1d4 al suo attacco
        print(f"{mago['classe']} lancia Concentrazione Assoluta! Aggiunge 1d4 al suo attacco.")
    else:
        print(f"{mago['classe']} tenta Concentrazione Assoluta, ma non ha successo.")

#Funzione per l'abilità del Ladro
def abilità_pugnali_acidi(ladro, avversari):
    dado = sum(random.randint(1, 4) for _ in range(2))
    if dado == 7 or dado == 8:
        for avversario in avversari:
            avversario["difesa"] = int(avversario["difesa"] * 0.75)  #Riduce la difesa del 25%
        print(f"{ladro['classe']} lancia Pugnali Acidi! Riduce la difesa degli avversari del 25%.")
    else:
        print(f"{ladro['classe']} non ha successo con Pugnali Acidi.")

#Funzione per l'abilità del Chierico
def abilità_favore_dei_dei(chierico, party):
    #Cura il personaggio più debole del party
    debole = min(party, key=lambda p: p["vita"])
    cura = random.randint(1, 6)
    debole["vita"] += cura
    print(f"{chierico['classe']} lancia Favore degli Dei! Cura {debole['classe']} di {cura} punti vita.")

#Funzione per eseguire un turno di combattimento
def esegui_turno(party1, party2):
    #Ordine degli attacchi
    for i in range(len(party1)):
        if party1[i]["vita"] > 0:
            attaccante = party1[i]
            difensore = party2[i]
            attacca(attaccante, difensore)
            
            #Attiviamo le abilità speciali
            if attaccante["classe"] == "Guerriero":
                abilità_berserk(attaccante)
            elif attaccante["classe"] == "Mago":
                abilità_concentrazione(attaccante)
            elif attaccante["classe"] == "Ladro":
                abilità_pugnali_acidi(attaccante, party2)
            elif attaccante["classe"] == "Chierico":
                abilità_favore_dei_dei(attaccante, party1)

#Funzione per verificare la vittoria
def verifica_vittoria(party1, party2):
    if all(p["vita"] <= 0 for p in party1):
        print("Il team 2 ha vinto!")
        return True
    elif all(p["vita"] <= 0 for p in party2):
        print("Il team 1 ha vinto!")
        return True
    return False

#Creiamo due squadre di personaggi
party1 = [crea_personaggio("Guerriero"), crea_personaggio("Mago"), crea_personaggio("Ladro"), crea_personaggio("Chierico")]
party2 = [crea_personaggio("Guerriero"), crea_personaggio("Mago"), crea_personaggio("Ladro"), crea_personaggio("Chierico")]

#Eseguiamo il combattimento a turni
turno = 1
while not verifica_vittoria(party1, party2):
    print(f"\nTurno {turno}")
    esegui_turno(party1, party2)
    turno += 1
