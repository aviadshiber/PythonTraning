# PythonTraning
this repo is my first repo.
in the following repo I will examine some small programs I write in Python. I will try to examin some power of the language. 

## Polynom
<p>
 the module will represent a Polynom simple operations like add,multiply and compose of other polynoms in time complexity of O(1), then it will be possible to evaluate the polynom in time complexity of O(n). 
    all this will be fairly easy and possible using lambda expressions & closures features in python :).
 </p>

### example of usage: </br>
 p1= Polynom()</br>
 p2= Polynom()</br>
 p1.add_monom(2,1)</br>
p2.add_monom(1,2).add_monom(5,0)</br>
p1.add(p2.get_block()) # p1(x)= 2x+x^2+5</br>
print p1.eval(2) #print 13</br>
p3=Polynom()</br>
p3.add_monom(5,2)</br>
p1.multiply(p3.get_block()) #p1(x) = 5x^2 *(2x+x^2+5)</br>
print p1.eval(2) # print 260</br>
p4=Polynom().add_monom(1,2)</br>
p1.compose(p4.get_block()) #p1(x)= 5(x^2)^2 * (2(x^2)+(x^2)^2+5)</br>
print p1.eval(2) # print 2320 </br>
