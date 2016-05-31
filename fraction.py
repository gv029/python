#a Fraction class based on the Object Oriented Programming chapter on interactivepython.org
#gv029

class Fraction:
    def __init__(self,numerator,denominator):

        self.num = numerator
        self.den = denominator

    def show(self):
        print self.num, "/", self.den


    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        def euclidGCD(a,b):
            if b == 0:
                return a;
            a_prime = a%b
            return euclidGCD(b,a_prime)
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = euclidGCD(newnum, newden)


        return Fraction(newnum//common,newden//common)




def main():
    myf = Fraction(3,5)

    f1 = Fraction(1,4)
    f2 = Fraction(1,2)

    f3 = f1 + f2
    print f3


main()
