class Rotor():
    def __init__(self,alphabet,wiring,notch):
        self.left = alphabet
        self.wiring = wiring
        self.notch = notch

    def forward(self,index):
        signal = self.wiring[index]
        ind = self.left.find(signal)
        return ind

    def backward(self,index):
        signal = self.left[index]
        ind = self.wiring.find(signal)
        return ind
