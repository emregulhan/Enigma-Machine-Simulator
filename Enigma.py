from Keyboard import Keyboard
from Plugboard import Plugboard


class Enigma:
    def __init__(self,keyboard,plug,rotors,rotorsList,ref,keySettings,alphabet,subs,ringSettings):
        for a,b in enumerate(keySettings):
            rotors[rotorsList[a]].rotate(b)
        self.ref = ref
        self.keyboard = keyboard
        self.plug = plug
        self.rotors = rotors
        self.rotorsList = rotorsList
        self.alphabet = alphabet
        self.keyboard = Keyboard(alphabet)
        self.plug.substitution(subs)
        self.ringSettings = ringSettings
    def encrypt(self,word):
        r1 = self.rotors[self.rotorsList[0]]
        r2 = self.rotors[self.rotorsList[1]]
        r3 = self.rotors[self.rotorsList[2]]

        r1.setRingSetting(self.ringSettings[0],self.alphabet)
        r2.setRingSetting(self.ringSettings[1],self.alphabet)
        r3.setRingSetting(self.ringSettings[2],self.alphabet)

        encrypted = ""
        for a in word:
            capitalized = a.isupper()
            if capitalized == False:
                a = a.upper()
            if a not in self.alphabet:
                encrypted += a
                continue

            if r3.left[0] == r3.notch and r2.left[0] == r2.notch:
                r3.rotate()
                r2.rotate()
                r1.rotate()
            elif r2.left[0] == r2.notch:
                r3.rotate()
                r2.rotate()
                r1.rotate()
            elif r3.left[0] == r3.notch:
                r3.rotate()
                r2.rotate()
            else:
                r3.rotate()
            index = self.keyboard.forward(a)
            index = self.plug.forward(index)
            index = r3.forward(index)
            index = r2.forward(index)
            index = r1.forward(index)
            index = self.ref.reflect(index)
            index = r1.backward(index)
            index = r2.backward(index)
            index = r3.backward(index)
            index = self.plug.backward(index)
            if capitalized == False:
                encrypted += self.keyboard.backward(index).lower()
            else:
                encrypted += self.keyboard.backward(index)

        return encrypted
