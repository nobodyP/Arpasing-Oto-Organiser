# DICT_COMB maker for Utau reorderer thingy
# Made in Python 3.10.5 by Psychic_Digit and NobodyP

PAIR_LIST = []
loopover = False
c_index = 0
v_index = 0

REF_DICT = {"aa":"V", "ae":"V", "ah":"V", "ao":"V", "ax":"V", "eh":"V", "er":"V", "ih":"V", "iy":"V", "uh":"V", "uw":"V", "aw":"V", "ay":"V", "ey":"V", "ow":"V", "oy":"V", "-":"V", "b":"C", "ch":"C", "d":"C", "dh":"C", "dx":"C", "f":"C", "g":"C", "hh":"C", "jh":"C", "k":"C", "l":"C", "m":"C", "n":"C", "ng":"C", "p":"C", "q":"C", "r":"C", "s":"C", "sh":"C", "t":"C", "th":"C", "v":"C", "w":"C", "y":"C", "z":"C", "zh":"C",}
REF_LIST = ("aa ae ah ao ax eh er ih iy uh uw aw ay ey ow oy - b ch d dh dx f g hh jh k l m n ng p q r s sh t th v w y z zh").split()

V_TUPLE = ("aa", "ae", "ah", "ao", "ax", "eh", "er", "ih", "iy", "uh", "uw", "aw", "ay", "ey", "ow", "oy", "-")
C_TUPLE = ("b", "ch", "d", "dh", "dx", "f", "g", "hh", "jh", "k", "l", "m", "n", "ng", "p", "q", "r", "s", "sh", "t", "th", "v", "w", "y", "z", "zh")


while loopover == False:
    for v_index in range(len(V_TUPLE)):
        
        print(str(c_index) + " " + str(v_index))
        
        PAIR_LIST.append(str(C_TUPLE[c_index]) + " " + str(V_TUPLE[v_index]))

        if c_index + v_index == 25 + 16:
            loopover = True
            break
            
        if v_index == 16:
            c_index += 1
            break

PAIR_TUPL = tuple(PAIR_LIST)
print(PAIR_TUPL)
print("done")
input()
