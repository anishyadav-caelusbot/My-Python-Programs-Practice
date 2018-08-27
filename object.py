class Box():
    def __init__(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def showD(self):
        print("length is", self.l)
        print("length is",self.w)
        print("length is",self.h)
    def vol(self):
        return self.l*self.w*self.h
b1=Box(4,5,6)
b1.showD()
print('volume is',b1.vol())

b2=Box(3,7,7)
b1.showD()
print('volume is',b1.vol())

b3=Box(9,8,4)
b1.showD()
print('volume is',b1.vol())


