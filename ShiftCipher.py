import sys
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def readFile(filename):
    with open(filename) as f:
        return f.readlines()


class ShiftCipher():

    def __init__(self,alphabet):
        self.ALPHABET = alphabet
    def compute_cipher(self,shift_amount): #SHIFTING THE LETTERS IN THE ALPHABET BY N TIMES TO THE RIGHT
        return self.ALPHABET[-1 * shift_amount:] + self.ALPHABET[:-1 * shift_amount]

    def encrypt_char(self,alphabet, cipher , letter):
        try:
            isUpper = letter.isupper()
            letter = letter.upper()
            indx = alphabet.index(letter)
            return cipher[indx] if isUpper else cipher[indx].lower()
        except Exception:
            return letter
    def encrypt_str(self,alphabet,cipher,str):
        encrypted = ""
        for a in str:
            encrypted += self.encrypt_char(alphabet=alphabet , cipher=cipher , letter=a)
        return encrypted
    def decrypt_str(self,alphabet,cipher,s):
        decrypted = ""
        for a in s:
            decrypted += self.encrypt_char(alphabet=cipher, cipher=alphabet , letter=a) #Switching alphabet and cipher parameters to decrypt the string.

        return decrypted


if __name__ == "__main__":
    (process, inp , shiftAmount) = (sys.argv[1],readFile(sys.argv[2]),sys.argv[3])
    shiftCipher = ShiftCipher(ALPHABET)
    cipher = shiftCipher.compute_cipher(int(shiftAmount))
    inp = "".join(inp)
    if(process == "encrypt"):
        print(shiftCipher.encrypt_str(ALPHABET,cipher,inp))
    if(process=="decrypt"):
        print(shiftCipher.decrypt_str(ALPHABET,cipher,inp))


