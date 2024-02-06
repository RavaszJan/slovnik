
zoznam={"CR":"Praha","SR":"Bratislava","Polsko":"Warsava"}


def pridaj(zoznam):
    country=input("Zadaj nazov statu:")
    city=input("Zadaj nazov hlavneho mesta:")
    zoznam.update([(country,city)])
    print(zoznam)

def odober(zoznam):
    print(zoznam)
    country=input("Zadaj nazov statu zo zoznamu na vymazanie:")
    del zoznam[country]
    print(zoznam)
def vyhladat(zoznam):
    nazov=dict(input("Zadaj nazov statu pre vyhladavanie:"))
    for i in zoznam:
        if i==nazov:
            print(zoznam.get[nazov])

def zmena(zoznam):
    print(zoznam)
    stat=input("Zadaj stat, ktory sa zmeni:")
    mesto=input("Zadaj nove city:")
    [stat]=mesto
    print(zoznam)


zmena(zoznam)