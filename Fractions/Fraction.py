import math #import the math module
# creating the class

# tbh a lot of this script was just make one code block, copy and paste and then slighty
# and then modify it to the usecase needed.
class Fraction:
    # initializing the class
    def __init__(self,numerator,denominator): # create the fraction
        self.numerator = numerator
        self.denominator = denominator # define / call both inside of the class
    def __eq__(self, other):
# now this is a cool way of commenting things, kinda, its a string, but still
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
        else: # just makes the actual fraction you can see the num and the denom and then the slash in between to seperate them
            if str(self.numerator)+'/'+str(self.denominator) == str(other): # looks a bit like spagetti, but its fine
                return True
            else:
                return False

    def __str__(self):
        self.simplify() # simplicaion of the fractions now
        result = str(self.numerator)+'/'+str(self.denominator) #takes the result and does the same thing as seen on LN 21
        return result
    def __add__(self, other):
        '''
        :param other: assuming that other variable is giving us a str value
        :return:
        '''
        # ^ more cool commenting (kinda)
        if isinstance(other, str): #catching the edge cases (but not really edgecases.) the left over stuff.
            nume = int(other.split('/')[0]) 
            deno = int(other.split('/')[1])
            if self.denominator == deno:
                new_nume = self.numerator + nume
                return str(new_nume) + '/' + str(deno)
            else:
                new_nume = (self.numerator* deno) + (nume * self.denominator)
                return str(new_nume) + '/'+ str(self.denominator * deno)
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
                return str(new_nume) + '/'+ str(self.denominator * deno)
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
                new_nume = (self.numerator * deno) - (nume * self.denominator)
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
                return str(new_nume) + '/'+ str(self.denominator * deno)
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
            new_frac.numerator = self.numerator * nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)
        elif isinstance(other,int):
            nume = other
            deno = 1
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator * nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)
    def __truediv__(self, other):
        # denominator and numerator would be reversed and multiply here;
        if isinstance(other, Fraction):
            nume = other.denominator
            deno = other.numerator
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator * nume
            new_frac.denominator = self.denominator * deno
            new_frac.simplify()
            return str(new_frac)
        elif isinstance(other,int):
            nume = 1
            deno = other
            new_frac = Fraction(self.numerator, self.denominator)
            new_frac.numerator = self.numerator * nume
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

print("woo, we can do math!")
# spageti code is my fav

