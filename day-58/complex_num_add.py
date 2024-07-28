class Complex:
    def __init__(self,real, img):
        self.real = real
        self.img = img
# 
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self , num2):
        addrealNum = self.real + num2.real
        addimgNum = self.img + num2.img
        return Complex(addrealNum,addimgNum)
    

    def __sub__(self , num2):
        addrealNum = self.real - num2.real
        addimgNum = self.img - num2.img
        return Complex(addrealNum,addimgNum)
    

    def __mul__(self , num2):
        addrealNum = self.real * num2.real
        addimgNum = self.img * num2.img
        return Complex(addrealNum,addimgNum)



num1 = Complex(3,5)
num1.showNumber()
num2 = Complex(1,4)
num2.showNumber()



num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

num5 = num1 * num2
num5.showNumber()



# this all when use jb dcoder nh use kren gn simmple methis hoga

# num3 = num1.add(num2)
# num3.showNumber()
# num4 = num1.sub(num2)
# num4.showNumber()
# num5 = num1.mul(num2)
# num5.showNumber()
