import random

hp_pers = 30
turni = 0

def lancia_dadi():
    dadi= random.randint(1,6)
    return dadi
while True:
    turni += 1
    print(f"turn:{turni}")
    if hp_pers > 0:
        dado = lancia_dadi()
        print(f"dameage taken:{dado}")
        hp_pers -= dado
        print(f"hp: {hp_pers}")
        if hp_pers <= 0:
            print("the character has been defeated!")
            break
