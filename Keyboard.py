class Keyboard():
    def __init__(self,alphabet):
        self.ALPHABET = alphabet

    def forward(self,letter):
        return self.ALPHABET.find(letter)

    def backward(self,index):
        return self.ALPHABET[index]

