

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

##
