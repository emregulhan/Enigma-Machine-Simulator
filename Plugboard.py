from SubstitutionCypher import SubstitutionCypher

class Plugboard():
    def __init__(self,alphabet):
        self.right = alphabet
        self.left = alphabet
    def substitution(self,str):
        substitionCypher = SubstitutionCypher()
        cipher = substitionCypher.compute_cipher((self.right),str)
        self.left = "".join(cipher)
        self.right = "".join(self.right)
    def forward(self,index):
        signal = self.right[index]
        ind = self.left.find(signal)
        return ind
    def backward(self,index):
        signal = self.left[index]
        ind = self.right.find(signal)
        return ind




