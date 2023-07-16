# Utau reorderer thingy
# Made in Python 3.10.5 by Psychic_Digit and NobodyP



# This is an old function thingy don't mess with it pls
old = """
def dict_comb_create(step):
    for i in range(43):

        if step == 42:
            print(PAIR_LIST)
            break
        if i == 42:
            i = 0
            step += 1

        PAIR_LIST.append("\"" + REF_LIST[step] + " " + REF_LIST[i] + "\"" + ":" + "\"" + REF_DICT[REF_LIST[step]] + REF_DICT[REF_LIST[i]] + "\"")
        return PAIR_LIST
"""



REF_DICT = {"aa":"V", "ae":"V", "ah":"V", "ao":"V", "ax":"V", "eh":"V", "er":"V", "ih":"V", "iy":"V", "uh":"V", "uw":"V", "aw":"V", "ay":"V", "ey":"V", "ow":"V", "oy":"V", "-":"V", "b":"C", "ch":"C", "d":"C", "dh":"C", "dx":"C", "f":"C", "g":"C", "hh":"C", "jh":"C", "k":"C", "l":"C", "m":"C", "n":"C", "ng":"C", "p":"C", "q":"C", "r":"C", "s":"C", "sh":"C", "t":"C", "th":"C", "v":"C", "w":"C", "y":"C", "z":"C", "zh":"C",}
REF_LIST = ("aa ae ah ao ax eh er ih iy uh uw aw ay ey ow oy - b ch d dh dx f g hh jh k l m n ng p q r s sh t th v w y z zh").split()

V = []
C = []
VC = []
CV = []
VV = []
CC = []

v_ = open("oto_sect/v_.txt", "w")
c_ = open("oto_sect/c_.txt", "w")
vc_ = open("oto_sect/vc_.txt", "w")
cv_ = open("oto_sect/cv_.txt", "w")
vv_ = open("oto_sect/vv_.txt", "w")
cc_ = open("oto_sect/cc_.txt", "w")


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

    for i in range(len(oto_con)):
        print(oto_con[i])



print()
print("length = " + str(len(oto_con)))
print("Entry #1 = " + str(oto_con[1]) + "\n")

pairch = input("Check for what phoneme combo?")
linech = int(input("Check in what line?"))

print("\n" + str(oto_con[linech]) + "\n")

if pairch in oto_con[linech]:
    print(str(pairch) + " found in " + str(linech) + "!")
    
    if REF_DICT[pairch] == "V":
        V.append(oto_con[linech])
        print("V")
        
    elif REF_DICT[pairch] == "C":
        C.append(oto_con[linech])
        print("C")
        
    elif REF_DICT[pairch] == "VC":
        VC.append(oto_con[linech])
        print("VC")
        
    elif REF_DICT[pairch] == "CV":
        CV.append(oto_con[linech])
        print("CV")
        
    elif REF_DICT[pairch] == "VV":
        VV.append(oto_con[linech])
        print("VV")
        
    else:
        CC.append(oto_con[linech])
        print("CC")


print(V + C + VC + CV + VV + CC)

v_.writelines(V)

v_.close()
c_.close()
vc_.close()
cv_.close()
vv_.close()
cc_.close()
