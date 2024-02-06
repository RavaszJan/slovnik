
zoznam={"CR":"Praha","SR":"Bratislava","Polsko":"Warsava"}


def pridaj(zoznam):
    country=input("Zadaj nazov statu pre pridanie:")
    city=input("Zadaj nazov hlavneho mesta:")
    zoznam.update([(country,city)])
    print(zoznam)

def odober(zoznam):
    print(zoznam)
    country=input("Zadaj nazov statu zo zoznamu na vymazanie:")
    del zoznam[country]
    print(zoznam)
def vyhladat(zoznam):
    stat=input("Zadaj nazov statu pre vyhladavanie:")
    if stat in zoznam:
        print(zoznam[stat])
    else:
        print("Stat sa nenasiel v zozname")



def zmena(zoznam):
    print(zoznam)
    stat=input("Zadaj stat, ktory sa zmeni:")
    mesto=input("Zadaj nove city:")
    zoznam[stat]=mesto
    print(zoznam)

pridaj(zoznam)
odober(zoznam)
vyhladat(zoznam)
zmena(zoznam)