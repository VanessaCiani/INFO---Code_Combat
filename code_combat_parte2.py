import random

def vita_giocatori():
    giocatore1 = random.randint(80, 101)
    giocatore2 = random.randint(80, 101)
    return giocatore1, giocatore2

def scudo():
    scudo1 = random.randint(5, 11)
    scudo2 = random.randint(5, 11)
    return scudo1, scudo2

def lancia_dadi(dadi, facce):
    lancio_dadi = []
    for _ in range(dadi):
        lancio_dadi.append(random.randint(1, facce))
    return sum(lancio_dadi)
    

giocatore1, giocatore2 = vita_giocatori()
scudo1, scudo2 = scudo()

print(f"la vita del giocatore 1 è: {giocatore1}")
print(f"la vita del giocatore 2 è: {giocatore2}")
print("\n")
print(f"lo sucdo del giocatore 1 è :{scudo1}")
print(f"lo sucdo del giocatore 1 è :{scudo1}")
print("\n")
turni_trascorsi = 0 

while giocatore1 > 0 and giocatore2 > 0:
    turni_trascorsi += 1
    print(f"Turno: {turni_trascorsi}")
    attacco_giocatore2 = lancia_dadi(2, 12)
    print(f"Danni causati al Giocatore1: {attacco_giocatore2}")
    danno_giocatore1 = (attacco_giocatore2 - scudo1)
    if danno_giocatore1 < 0:
        danno_giocatore1 == 0
    print(f"Vita rimanente Giocatore1: {giocatore1}")   
    attacco_giocatore1 = lancia_dadi(4, 6)
    print(f"Danni causati al Giocatore2: {attacco_giocatore1}")
    danno_giocatore2 = attacco_giocatore1 - scudo2
    if danno_giocatore2 < 0:
        danno_giocatore2 == 0
    giocatore2 -= danno_giocatore2
    print(f"Vita rimanente Giocatore2: {giocatore2}")
    
if giocatore1 <= 0:
    print("Il Giocatore2 ha vinto!")
else:
    print("Il Giocatore1 ha vinto!")
