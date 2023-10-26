import sys

# (mode,filename,key) = (sys.argv[0],sys.argv[1],sys.argv[2])

reflectors = {"A":"EJMZALYXVBWFCRQUONTSPIKHGD","B":"YRUHQSLDPXNGOKMIEBFZCWVJAT","C":"FVPJIAOYEDRZXWGCTKUQSBNMHL"}
rotors = {"I":"EKMFLGDQVZNTOWYHXUSPAIBRCJ","II":"AJDKSIRUXBLHWTMCQGZNPYFVOE","III":"BDFHJLCPRTXVZNYEIWGAKMUSQO","IV":"ESOVPZJAYQUIRHXLNFTGKDCMWB","V":"VZBRGITYUPSDNHLXAWMJQOFECK"}


alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ALPHABET = list(alphabetString)
with open('raw_text_file.txt') as f:
    lines = f.readlines()

def readFile(filename):
    with open(filename) as f:
        return f.readlines()

class ShiftCipher():
    def compute_cipher(self,shift_amount): #SHIFTING THE LETTERS IN THE ALPHABET BY N TIMES TO THE RIGHT
        return ALPHABET[-1 * shift_amount:] + ALPHABET[:-1 * shift_amount]

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
            encrypted += self.encrypt_char(alphabet , cipher , a)

        return encrypted
    def decrypt_str(self,alphabet,cipher,s):
        decrypted = ""
        for a in s:
            decrypted += self.encrypt_char(cipher, alphabet , a) #Switching alphabet and cipher parameters to decrypt the string.

        return decrypted

class SubstitutionCypher():
    def compute_cipher(self,alphabet,pair):
        temp = pair.split("-")
        cipher = alphabet.copy() ## BE CAREFUL HERE.
        for a in temp:
            cipher[alphabet.index(a[0])] = a[1]

        return cipher

##
shiftCipher = ShiftCipher()

shiftCipher.cipher = shiftCipher.compute_cipher(20)  ## Test.
output = ""
for a in lines:
    output += (shiftCipher.encrypt_str(ALPHABET,shiftCipher.cipher,a)) ## Test.

print(output)
##


##
substituionCypher = SubstitutionCypher()
#print(substituionCypher.compute_cipher(ALPHABET,"AR-GK-OX"))

##
#Ajsn, Anin Anhn.
