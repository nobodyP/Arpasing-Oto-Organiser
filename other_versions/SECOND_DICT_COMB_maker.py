# DICT_COMB maker for Utau reorderer thingy
# Made in Python 3.10.5 by Psychic_Digit and NobodyP

PAIR_LIST = []
loopover = False
first_unit = 0

REF_DICT = {"aa":"V", "ae":"V", "ah":"V", "ao":"V", "ax":"V", "eh":"V", "er":"V", "ih":"V", "iy":"V", "uh":"V", "uw":"V", "aw":"V", "ay":"V", "ey":"V", "ow":"V", "oy":"V", "-":"V", "b":"C", "ch":"C", "d":"C", "dh":"C", "dx":"C", "f":"C", "g":"C", "hh":"C", "jh":"C", "k":"C", "l":"C", "m":"C", "n":"C", "ng":"C", "p":"C", "q":"C", "r":"C", "s":"C", "sh":"C", "t":"C", "th":"C", "v":"C", "w":"C", "y":"C", "z":"C", "zh":"C",}
REF_LIST = ("aa ae ah ao ax eh er ih iy uh uw aw ay ey ow oy - b ch d dh dx f g hh jh k l m n ng p q r s sh t th v w y z zh").split()

while loopover == False:
    for second_unit in range(len(REF_LIST)):

        if REF_DICT[REF_LIST[second_unit]] == "V":
            if REF_DICT[REF_LIST[first_unit]] == "V":

                PAIR_LIST.append(str(REF_LIST[first_unit]) + " " + str(REF_LIST[second_unit]))

        if second_unit == 17:
            first_unit += 1
            break

        if first_unit + second_unit == 34:
            loopover = True
            break

PAIR_TUPL = tuple(PAIR_LIST)
print(PAIR_TUPL)
print("done")
