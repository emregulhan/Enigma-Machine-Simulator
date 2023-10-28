from Reflector import Reflector
from ShiftCipher import ShiftCipher
from SubstitutionCypher import SubstitutionCypher
from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Enigma import Enigma

# (mode,filename,key) = (sys.argv[0],sys.argv[1],sys.argv[2])
word = input("Kelime giriniz: ")
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

reflectorA = Reflector(ALPHABET,"EJMZALYXVBWFCRQUONTSPIKHGD")
reflectorB = Reflector(ALPHABET,"YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorC = Reflector(ALPHABET,"FVPJIAOYEDRZXWGCTKUQSBNMHL")
reflectors = {"A":reflectorA,"B":reflectorB,"C":reflectorC}

rotor_I = Rotor(ALPHABET,"EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
rotor_II = Rotor(ALPHABET,"AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
rotor_III = Rotor(ALPHABET,"BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
rotor_IV = Rotor(ALPHABET,"ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
rotor_V = Rotor(ALPHABET,"VZBRGITYUPSDNHLXAWMJQOFECK ","Z")
rotors = {"I":rotor_I,"II":rotor_II,"III":rotor_III,"IV":rotor_IV,"V":rotor_V}

rotorsList = ["I","II","III"]

keyboard = Keyboard(ALPHABET)
plugboard = Plugboard(ALPHABET)
reflector = reflectorB #IT IS A PARAMETER
keySettings = "AAA"
subs = "AR GK OX"
enigma = Enigma(keyboard,plugboard,rotors,rotorsList,reflector,keySettings,ALPHABET,subs)
enigma.encrypt(word)
print("This is the ENIGMA")


keySettings = "AAA"
for a,b in enumerate(keySettings):
    rotors[rotorsList[a]].rotate(b)


print("DENEMELERRRR")


keyboard = Keyboard(ALPHABET)
plugboard = Plugboard(ALPHABET)
plugboard.substitution("AR GK OX")

encrpyted = ""
"""for a in word:
    if a not in ALPHABET:
        encrpyted += a
        continue

    if rotor_III.left[0] == rotor_III.notch and rotor_II.left[0] == rotor_II.notch:
        rotor_III.rotate()
        rotor_II.rotate()
        rotor_I.rotate()
    elif rotor_III.left[0] == rotor_III.notch:
        rotor_III.rotate()
        rotor_II.rotate()
    else:
        rotor_III.rotate()

    index = keyboard.forward(a)
    index = plugboard.forward(index)
    index = rotors["III"].forward(index)
    index = rotors["II"].forward(index)
    index = rotors["I"].forward(index)
    index = reflectorB.reflect(index)
    index = rotors["I"].backward(index)
    index = rotors["II"].backward(index)
    index = rotors["III"].backward(index)
    index = plugboard.backward(index)

    print("**********")
    print(keyboard.backward(index))
    encrpyted += keyboard.backward(index)


print(encrpyted)"""

"""with open('raw_text_file.txt') as f:
    lines = f.readlines()

def readFile(filename):
    with open(filename) as f:
        return f.readlines()

def encrypt_file(filename,alphabet,n=0,cipher=None):
    if cipher==None:
        cipher = shiftCipher.compute_cipher(n)
    lines = readFile(filename)
    output = ""
    for a in lines:
        output += (shiftCipher.encrypt_str(alphabet=alphabet,cipher=cipher,str=a))
    return output

def decrypt_file(filename,alphabet,n=0,cipher=None):
    if cipher==None:
        cipher = shiftCipher.compute_cipher(n)
    lines = readFile(filename)
    output = ""
    for a in lines:
        output += (shiftCipher.encrypt_str(alphabet=cipher,cipher=alphabet,str=a))
    return output"""



#shiftCipher = ShiftCipher(ALPHABET)



##


##
"""substituionCypher = SubstitutionCypher()
newcipher = (substituionCypher.compute_cipher(ALPHABET,"VZ-YD-EO"))
print(encrypt_file('raw_text_file.txt',ALPHABET,cipher=newcipher))"""


##
#Ajsn, Anin Anhn.
