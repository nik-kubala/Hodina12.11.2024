fero = "shakjb jkhjvvhj,h§ds§fsoif"

for i in range(0, len(fero)):
        print(fero[i])


for i in fero:
    print(i)


for key,content in enumerate(fero):             #ako prechadzat string fero
        print(key,content)


i = 0
while i < len(fero):
    i += 1

    # Uloha 1
    # a = input("Zadaj mi číslo")
    scitanie = 0


    # for cislica in a:
    # scitanie += int(cislica)
    # print(scitanie)

    # Uloha 2
    def shreder(ret):
        samo = "aeiyou"
        for i in samo:
            print("samohlaska", i, "sa tam nachádza", ret.count(i))
        # a = input("Zadaj mi slovo")
        # shreder(a)

        # x = input("Zadaj mi vetu so zátvorkou")
        # def vpisanie(ret):
        y = x.find("(")
        z = x.find(")")
        if z - y > 0:
            vysledok = x[y:z + 1:]
            # print(vysledok)
        while x.find("(") != -1:
            slice = x[:y:] + x[z + 1::]
            print(slice)


    # vpisanie(x)

    x = input("Zadaj mi vetu so zátvorkou")


    def vpisanie(ret):
        while x.find("(") != -1:
            y = x.find("(")
            z = x.find(")")
        slice = x[:y:] + x[z + 1::]
        print(slice)
vpisanie(x)





fero = "jelenovipivonelej"

jano = fero[::-1]                # [štart:koniec:krok]
#print(jano)

a = "ahoj"
i = 0
while i < len(a):
    i += 1
    b = a[:i:]
    #print(b)

#alebo

#a = input("napis mi nieco")
#for x in range(0, len(a)+1):
    #print(a[:x:])

m = input("Zadaj:")
i = len(a)
while i > 0:
    i = i - 1
    z = m[i::]
    print(z)