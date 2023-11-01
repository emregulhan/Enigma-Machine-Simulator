import sys
from ShiftCipher import ShiftCipher

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def readFile(filename):
    with open(filename) as f:
        return f.readlines()


class SubstitutionCypher():
    def compute_cipher(self,alphabet,pair):
        temp = pair.split(" ")
        cipher = alphabet
        for a in temp:
            index_1 = alphabet.find(a[0])
            index_2 = alphabet.find(a[1])
            cipher = cipher[:index_1] + a[1] + cipher[index_1+1:]
            cipher = cipher[:index_2] + a[0] + cipher[index_2+1:]
        return cipher

if __name__ == "__main__":
    (process, inp , subs) = (sys.argv[1],readFile(sys.argv[2]),sys.argv[3])
    subs = subs.split("-")
    subs = " ".join(subs)
    substitionCypher = SubstitutionCypher()
    shiftCipher = ShiftCipher(ALPHABET)
    if process == "encrypt":
        cipher = substitionCypher.compute_cipher(ALPHABET,subs)
        inp = "".join(inp)
        print(shiftCipher.encrypt_str(ALPHABET,cipher,inp))

    elif process == "decrypt":
        cipher = substitionCypher.compute_cipher(ALPHABET,subs)
        inp = "".join(inp)
        print(shiftCipher.decrypt_str(ALPHABET,cipher,inp))
