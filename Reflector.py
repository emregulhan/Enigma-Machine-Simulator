class Reflector():
    def __init__(self,alphabet,wiring):
        self.left = alphabet
        self.wiring = wiring

    def reflect(self,index):
        signal = self.left[index]
        ind = self.wiring.find(signal)
        return ind
