import sys

from Reflector import Reflector
from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Enigma import Enigma

def readFile(filename):
    with open(filename) as f:
        return f.readlines()


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Rotors
rotor_I = Rotor(ALPHABET,"EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
rotor_II = Rotor(ALPHABET,"AJDKSIRUXBLHWTMCQGZNPYFVOE","E")
rotor_III = Rotor(ALPHABET,"BDFHJLCPRTXVZNYEIWGAKMUSQO","V")
rotor_IV = Rotor(ALPHABET,"ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
rotor_V = Rotor(ALPHABET,"VZBRGITYUPSDNHLXAWMJQOFECK ","Z")
rotors = {"I":rotor_I,"II":rotor_II,"III":rotor_III,"IV":rotor_IV,"V":rotor_V}

#Reflectors
reflectorA = Reflector(ALPHABET,"EJMZALYXVBWFCRQUONTSPIKHGD")
reflectorB = Reflector(ALPHABET,"YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorC = Reflector(ALPHABET,"FVPJIAOYEDRZXWGCTKUQSBNMHL")
reflectors = {"A":reflectorA,"B":reflectorB,"C":reflectorC}


#Keyboard and plugboard
keyboard = Keyboard(ALPHABET)
plugboard = Plugboard(ALPHABET)




(settings,inputText) = (readFile(sys.argv[1]),readFile(sys.argv[2]))

#Choosing which rotors will be used
rotorsList = settings[0].strip("\n").split("-")

#Choosing which reflector will be used
reflector = reflectors[settings[1].strip("\n")]


#Starting settings of Rotors.
keySettings = settings[2].strip("\n")

#Setting the ring settings.
ringSettings = settings[3].strip("\n").split(",")
for a in range(3):
    ringSettings[a] = int(ringSettings[a])


#Substitions
subs = settings[4].strip("\n")


word = "\n".join(inputText)


#Creating our enigma machine and encrypting a string with that enigma machine.
enigma = Enigma(keyboard,plugboard,rotors,rotorsList,reflector,keySettings,ALPHABET,subs,ringSettings)
print("Encrypted: " , enigma.encrypt(word))






