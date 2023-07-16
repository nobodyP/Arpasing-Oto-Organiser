# DICT_COMB maker for Utau reorderer thingy
# Made in Python 3.10.5 by Psychic_Digit and NobodyP

PAIR_LIST = []
loopover = False
step = 0
step_inc_check = 0

REF_DICT = {"aa":"V", "ae":"V", "ah":"V", "ao":"V", "ax":"V", "eh":"V", "er":"V", "ih":"V", "iy":"V", "uh":"V", "uw":"V", "aw":"V", "ay":"V", "ey":"V", "ow":"V", "oy":"V", "-":"V", "b":"C", "ch":"C", "d":"C", "dh":"C", "dx":"C", "f":"C", "g":"C", "hh":"C", "jh":"C", "k":"C", "l":"C", "m":"C", "n":"C", "ng":"C", "p":"C", "q":"C", "r":"C", "s":"C", "sh":"C", "t":"C", "th":"C", "v":"C", "w":"C", "y":"C", "z":"C", "zh":"C",}
REF_LIST = ("aa ae ah ao ax eh er ih iy uh uw aw ay ey ow oy - b ch d dh dx f g hh jh k l m n ng p q r s sh t th v w y z zh").split()

while loopover == False:      
    for i in range(43):
        
        PAIR_LIST.append("\"" + REF_LIST[step] + " " + REF_LIST[i] + "\"" + ":" + "\"" + REF_DICT[REF_LIST[step]] + REF_DICT[REF_LIST[i]] + "\"")

        #print(PAIR_LIST[i])

        if step + i == 84:
            loopover = True
            break
        if i == 42:
            print(step)
            step += 1

print(PAIR_LIST)
print("done")
