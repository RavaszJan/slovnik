import pickle

zoznam = {"CR": "Praha", "SR": "Bratislava", "Polsko": "Warsava", "Madarsko": "Budapest"}


def pridaj(zoznam):
    print(zoznam)
    country = input("Zadaj nazov statu:")
    city = input("Zadaj nazov hlavneho mesta:")
    zoznam.update([(country, city)])
    print(zoznam)


def odober(zoznam):
    print(zoznam)
    country = input("Zadaj nazov statu zo zoznamu na vymazanie:")
    del zoznam[country]
    print("Stat:{} bol vymazany zo zoznamu".format(country))
    print(zoznam)


def vyhladat(zoznam):
    stat = input("Zadaj nazov statu pre vyhladavanie:")
    if stat in zoznam:
        print(zoznam[stat])
    else:
        print("Stat sa nenasiel v zozname")


def zmena(zoznam):
    print(zoznam)
    stat = input("Zadaj stat, ktory sa zmeni:")
    mesto = input("Zadaj nove city:")
    zoznam[stat] = mesto
    print(zoznam)


def vloz_do_suboru(nazov_suboru):
    with open(nazov_suboru, "wb") as file:
        pickle.dump(zoznam, file)
        print(zoznam)


def vytvor_zo_suboru(nazov_suboru):
    with open(nazov_suboru, "rb") as file:
        return pickle.load(file)


# pridaj(zoznam)
# odober(zoznam)
# vyhladat(zoznam)
# zmena(zoznam)
vloz_do_suboru("country.txt")
print(vloz_do_suboru)
obnov = vytvor_zo_suboru("country.txt")
print(obnov)