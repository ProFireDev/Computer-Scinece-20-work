import math
#creating the class
class Fraction:
    #initializing the class
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __eq__(self, other):
        '''
        :param other: the second fraction to be compared with the one constructed
        from class vars
        :return:
        '''
        if isinstance(other, str):
            if str(self.numerator) + '/' + str(self.denominator) == str(other):
                return True
            else:
                return False
        else:
            if str(self.numerator/self.denominator) == str(other):
                return True
            else:
                return False

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)+' ->'+' '+str(self.numerator/self.denominator)
    def __add__(self, other):
        '''
        :param other: assuming that other variable is giving us a str value
        :return:
        '''
        if isinstance(other, str):
            nume = int(other.split('/')[0])
            deno = int(other.split('/')[1])
            if self.denominator == deno:
                new_nume = self.numerator + nume
                return str(new_nume) + '/' + str(deno)
            else:
                new_nume = (self.numerator* deno) + (nume * self.denominator)
                return str(new_nume) + '/'+ str(self.denominator*deno)
        elif isinstance(other,float):
            return self.numerator/self.denominator + other
        elif isinstance(other, int):
            nume = other
            deno = 1
            if self.denominator == deno:
                new_nume = self.numerator + nume
                return str(new_nume) + '/' + str(deno)
            else:
                new_nume = (self.numerator* deno) + (nume * self.denominator)
                return str(new_nume) + '/'+ str(self.denominator*deno)
    def __sub__(self, other):
        '''
        :param other: assuming that other variable is giving us a str value
        :return:
        '''
        if isinstance(other, str):
            nume = int(other.split('/')[0])
            deno = int(other.split('/')[1])
            if self.denominator == deno:
                new_nume = self.numerator - nume
                return str(new_nume) + '/' + str(deno)
            else:
                new_nume = (self.numerator* deno) - (nume * self.denominator)
                return str(new_nume) + '/'+ str(self.denominator*deno)
        elif isinstance(other, float):
            return self.numerator/self.denominator - other

        elif isinstance(other, int):
            nume = other
            deno = 1
            if self.denominator == deno:
                new_nume = self.numerator - nume
                return str(new_nume) + '/' + str(deno)
            else:
                new_nume = (self.numerator* deno) - (nume * self.denominator)
                return str(new_nume) + '/'+ str(self.denominator*deno)
    def __mul__(self, other):
        if isinstance(other, str):
            nume = int(other.split('/')[0])
            deno = int(other.split('/')[1])
            return str(self.numerator*nume) + '/' + str(self.denominator*deno)
        elif isinstance(other, float):
            return self.numerator/self.denominator * other
        elif isinstance(other,int):
            return str(self.numerator*other) +'/'+str(self.denominator)
    def __truediv__(self, other):
        #denominator and numerator would be reversed and multiply here;
        if isinstance(other, str):
            nume = int(other.split('/')[1])
            deno = int(other.split('/')[0])
            return str(self.numerator*nume) + '/' + str(self.denominator*deno)
        elif isinstance(other, float):
            return self.numerator/self.denominator * other
        elif isinstance(other,int):
            return str(self.numerator*other) +'/'+str(self.denominator)
    def toDecimal(self):
        return self.numerator/self.denominator
    def simplify(self):
        compute_gcd = math.gcd(self.numerator,self.denominator)
        #reduce the fraction and assign it
        #assing integers
        self.numerator = int(self.numerator/compute_gcd)
        self.denominator = int(self.denominator/compute_gcd)


f = Fraction(5,10)
f.simplify()
print(f.numerator,f.denominator)
