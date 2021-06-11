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
        if isinstance(other,Fraction):
            if str(self) == str(other):
                return True
            else:
                return False
        else:
            if str(self.numerator)+'/'+str(self.denominator) == str(other):
                return True
            else:
                return False

    def __str__(self):
        self.simplify()
        result = str(self.numerator)+'/'+str(self.denominator)
        return result
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
        elif isinstance(other, Fraction):
            nume = other.numerator
            deno = other.denominator
            if self.denominator == deno:
                new_nume = self.numerator + nume
                new_nume = (self.numerator * deno) + (nume * self.denominator)
                new_frac = Fraction(self.numerator, self.denominator)
                new_frac.numerator = new_nume
                new_frac.denominator = self.denominator
                new_frac.simplify()
                return str(new_frac)

            else:
                new_nume = (self.numerator * deno) + (nume * self.denominator)
                new_frac = Fraction(self.numerator,self.denominator)
                new_frac.numerator = new_nume
                new_frac.denominator = self.denominator * deno
                new_frac.simplify()
                return str(new_frac)
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
        elif isinstance(other, Fraction):
            nume = other.numerator
            deno = other.denominator
            if self.denominator == deno:
                new_nume = self.numerator - nume
                new_frac = Fraction(self.numerator, self.denominator)
                new_frac.numerator = new_nume
                new_frac.denominator = self.denominator
                new_frac.simplify()
                return str(new_frac)
            else:
                new_nume = (self.numerator * deno) - (nume * self.denominator)
                new_frac = Fraction(self.numerator, self.denominator)
                new_frac.numerator = new_nume
                new_frac.denominator = self.denominator * deno
                new_frac.simplify()
                return str(new_frac)
        elif isinstance(other, float):
            return self.numerator/self.denominator - other
    def __mul__(self, other):

        if isinstance(other, Fraction):
            nume = other.numerator
            deno = other.denominator
            new_frac = Fraction(self.numerator,self.denominator)
            new_frac.numerator = self.numerator*nume
            new_frac.denominator = self.denominator*deno
            new_frac.simplify()
            return str(new_frac)
        elif isinstance(other,int):
            nume = other
            deno = 1
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator*nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)
    def __truediv__(self, other):
        #denominator and numerator would be reversed and multiply here;
        if isinstance(other, Fraction):
            nume = other.denominator
            deno = other.numerator
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator*nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)
        elif isinstance(other,int):
            nume = 1
            deno = other
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator*nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)

    def toDecimal(self):
        return self.numerator/self.denominator
    def simplify(self):
        compute_gcd = math.gcd(self.numerator,self.denominator)
        # reduce the fraction and assign it
        # assing integers
        self.numerator = int(self.numerator/compute_gcd)
        self.denominator = int(self.denominator/compute_gcd)
        return self







