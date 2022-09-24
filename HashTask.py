import numpy as np
import os

def custom_hash(line):
    line = list(line)
    res = np.uint16(0)


    for i in range(0 , len(line)):
        line[i] = ((ord(line[i]) >> 1) & 1) + ((ord(line[i]) >> 3) & 1) + ((ord(line[i]) >> 5) & 1) + ((ord(line[i]) >> 7) & 1)
        if (line[i] % 2 == 0):
            line[i] = 0
        else:
            line[i] = 1
        res = res << 1
        res = res | line[i]
        res = res & 0xFFFF

    return(res)

def ht():

    coll = 0
    un = 0
    un_list = []
    h_list = []
    x = 0
    hash_res = ""
    f = open('words.txt')
    anim = 0
    line = f.readline()
    while (line != ""):
        hash_res = bin(custom_hash((line.split('\n')[0])))
        if hash_res not in un_list:
            un_list += [hash_res]
            un += 1
        else:
            coll += 1
        h_list += [hash_res]
        x += 1
        line = f.readline()


        if anim == 5000:
            os.system('cls||clear')
            print("  \  Идёт обработка, подождите")
        elif anim == 10000:
            os.system('cls||clear')
            print("  |  Идёт обработка, подождите.")
        elif anim == 15000:
            os.system('cls||clear')
            print("  /  Идёт обработка, подождите..")
        elif anim == 20000:
            os.system('cls||clear')
            print("  -  Идёт обработка, подождите...")
            anim = 0
        anim += 1
    print(h_list)
    print("\nОбработано " + str(x) + " строк. Количество коллизий - " + str(coll) + ". Количество уникальных hash значений - " + str(un))
    print()