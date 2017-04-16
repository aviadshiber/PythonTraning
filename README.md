# PythonTraning
his repo is my first repo, which will examine some short program with perhaps big power.

## Polynom
 the module will represent a Polynom simple operations like add,multiply and compose of other polynoms in time complexity of O(1), then it will be possible to evaluate the polynom in time complexity of O(n). 
    all this will be fairly easy and possible using lambda expressions & closures features in python :).

###example of usage:
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
