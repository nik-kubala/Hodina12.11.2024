def velkepismena():
    x = input("Zadaj mi slovíčko:")
    velkePismenka = "ABCDEFGHIYJKLMNOPQRSTUWXYZ"
    for i in velkePismenka:
        if i in x:
            print("Veľké písmenko", i, "sa tam nachádza", x.count(i))
#velkepismena()


def odstranovac():
    y = input("Zadaj mi slovko: ")
    samohlasky = "aeiyouAEIYOU"
    for i in samohlasky:
        while i in y:
            pozicia = y.find(i)
            y = y[:pozicia] + y[pozicia + 1:]
    return y
vysledok = odstranovac()
#print("Reťazec bez samohlások:", vysledok)


def vety():
    z = input("Zadaj mi vety:")
    znamienka = ".?!"
    for i in znamienka:
        if i in z:
            print("Veta s", i, "sa tam nachádza", z.count(i))
#vety()

