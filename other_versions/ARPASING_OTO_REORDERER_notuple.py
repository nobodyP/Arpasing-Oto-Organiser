# Utau reorderer thingy
# Made in Python 3.10.5 by Psychic_Digit and NobodyP
import json

SOLO_REF_DICT = {"aa":"V", "ae":"V", "ah":"V", "ao":"V", "ax":"V", "eh":"V", "er":"V", "ih":"V", "iy":"V", "uh":"V", "uw":"V", "aw":"V", "ay":"V", "ey":"V", "ow":"V", "oy":"V", "-":"V", "b":"C", "ch":"C", "d":"C", "dh":"C", "dx":"C", "f":"C", "g":"C", "hh":"C", "jh":"C", "k":"C", "l":"C", "m":"C", "n":"C", "ng":"C", "p":"C", "q":"C", "r":"C", "s":"C", "sh":"C", "t":"C", "th":"C", "v":"C", "w":"C", "y":"C", "z":"C", "zh":"C"}
SOLO_REF_TUPLE = tuple(SOLO_REF_DICT.keys())

V = []
C = []
VC = []
CV = []
VV = []
CC = []

v_ = open("oto_split/v_.txt", "w")
c_ = open("oto_split/c_.txt", "w")
vc_ = open("oto_split/vc_.txt", "w")
cv_ = open("oto_split/cv_.txt", "w")
vv_ = open("oto_split/vv_.txt", "w")
cc_ = open("oto_split/cc_.txt", "w")


#Start of program
print("Arpasing Oto Reorder")
print("Made by Psychic_Digit and NobodyP")
print("1/12/23 Python 3.10.5\n")

input("Make sure you have a oto.txt file\nin the directory of this program.\nAn oto.ini file can be converted\ninto a oto.txt file and vice versa.\nPress Enter >> ")
print("\n")




# make sure to add a system so that if you dont have a oto.txt it tells you and exits out
oto = open("oto.txt", "r")
oto_con = oto.readlines()

if input("Read the contents of oto.txt? (\"y\" for Yes)") == "y":
        print(str(oto_con))



temp = """
print()
print("length = " + str(len(oto_con)))
print("Entry #1 = " + str(oto_con[1]) + "\n")

pairch = input("Check for what phoneme combo?")
linech = int(input("Check in what line?"))

print("\n" + str(oto_con[linech]) + "\n")

if pairch in oto_con[linech]:
    print(str(pairch) + " found in " + str(linech) + "!")
    
    if SOLO_REF_DICT[pairch] == "V":
        V.append(oto_con[linech])
        print("V")
        
    elif SOLO_REF_DICT[pairch] == "C":
        C.append(oto_con[linech])
        print("C")
        
    elif SOLO_REF_DICT[pairch] == "VC":
        VC.append(oto_con[linech])
        print("VC")
        
    elif SOLO_REF_DICT[pairch] == "CV":
        CV.append(oto_con[linech])
        print("CV")
        
    elif SOLO_REF_DICT[pairch] == "VV":
        VV.append(oto_con[linech])
        print("VV")
        
    else:
        CC.append(oto_con[linech])
        print("CC")
"""

print(CC_TUPLE)
print(V + C + VC + CV + VV + CC)

v_.writelines(V)
c_.writelines(C)
vc_.writelines(VC)
cv_.writelines(CV)
vv_.writelines(VV)
cc_.writelines(CC)

v_.close()
c_.close()
vc_.close()
cv_.close()
vv_.close()
cc_.close()
