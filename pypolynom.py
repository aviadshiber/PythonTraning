class Polynom(object):
    """
    the module will represent a Polynom with simple operations like add,multiply and compose of other polynoms in time complexity of O(1), then it will be possible to evaluate the polynom in time complexity of O(n). 
    all this will be fairly easy and possible using lambda expressions & closures features in python :).
    """
    def __init__(self):
        self.block = (lambda x: 0)

    def get_block(self):
        """
        the method will return the representation of the polynom as a function
        :return: a polynom as a function
        """
        return self.block

    def add(self, other_block):
        """
        the method will add another polynom block to this polynom
        Time complexity O(1) Space complexity: O(1)
        :param other_block: the block of the other polynom
        :return: self polynom
        """
        current = self.block
        self.block = (lambda x: current(x) + other_block(x))
        return self

    def add_monom(self, coef , exp):
        """
        the method will add a monom to the this polynom
        Time complexity O(1) Space complexity: O(1)
        :param coef: the coef of x
        :param exp: the exp of x
        :return: this object
        """
        monom = (lambda x: coef * (x ** exp))
        current = self.block
        self.block = lambda x: current(x) + monom(x)
        return self

    def multiply(self, other_block):
        """
        the method will multiply this polynom with other polynom block.
        Time complexity O(1) Space complexity: O(1)
        :param other_block: the block of the other polynom
        :return: this polynom after multiplication
        """
        current = self.block
        self.block = lambda x: (current(x)) * (other_block(x))
        return self

    def compose(self, other_block):
        """
        the method wil compose this polynom with other polynom block.
        for example if the polynom is now p(x) then after composing it will be p(g(x)).
        Time complexity O(1) Space complexity: O(1)
        :param other_block: the block of the other polynom
        :return: this polynom after composition
        """
        current = self.block
        self.block = lambda x: current(other_block(x))
        return self

    def eval(self,x):
        """
        the method evaluates the polynom with value of x.
        Time complexity O(n) Space complexity O(1)
        :param x: the value to evaluate the Polynom with. 
        :return: the result of the evaluation.
        """
        return self.block(x)


#example of usage:
p1= Polynom()
p2= Polynom()
p1.add_monom(2,1)
p2.add_monom(1,2).add_monom(5,0)
p1.add(p2.get_block()) # p1(x)= 2x+x^2+5
print p1.eval(2) #print 13
p3=Polynom()
p3.add_monom(5,2)
p1.multiply(p3.get_block()) #p1(x) = 5x^2 *(2x+x^2+5)
print p1.eval(2) # print 260
p4=Polynom().add_monom(1,2)
p1.compose(p4.get_block()) #p1(x)= 5(x^2)^2 * (2(x^2)+(x^2)^2+5)
print p1.eval(2) # print 2320




