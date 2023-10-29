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

    def rotate(self,rotateTo=""):
        if rotateTo=="":
            self.left = self.left[1:] + self.left[0]
            self.wiring = self.wiring[1:] + self.wiring[0]
        else:
            indx = self.left.find(rotateTo)
            self.left = self.left[indx:] + self.left[:indx]
            self.wiring = self.wiring[indx:] + self.wiring[:indx]
    def setRingSetting(self,n,alphabet):
        if n==1:
            return
        else:
            shf = n-1
            #Shifting alphabet, cipher backwards
            self.left = self.left[-1 * shf:] + self.left[:-1*shf]
            self.wiring = self.wiring[-1 * shf:] + self.wiring[:-1*shf]
            #Shifting the notch point
            notchIndex = alphabet.find(self.notch)
            self.notch = alphabet[(notchIndex-n+1) % 26]
