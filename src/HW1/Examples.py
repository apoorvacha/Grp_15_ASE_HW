from Num import Num
from Sym import Sym
from Start import the
from Misc import *


def test_nums():
    val = Num()
    lst = [1,1,1,1,2,2,3]
    for a in lst:
        val.add(a)
    if(11/7 == val.mid() and 0.787 == rnd(val.div())):
        print("test_nums : pass")
        return True
    return False
    
def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    if("a"==sym1.mid() and 1.379 == rnd(sym1.div())):
        print("test_sym : pass")
        return True
    return False
    

def test_rand():
    num1 = Num()
    num2 = Num()
    seed = the["seed"]
    for i in range(1,1000):
        num1.add(rand(0,1))
    seed = the["seed"]
    for i in range(1,1000):
        num2.add(rand(0,1))
    m1 = rnd(num1.mid(), 10) 
    m2 = rnd(num2.mid(),10)
    if(m1 == m2 and 0.6 == rnd(m1,1)):
        print("test_rand : pass")
        return True
    return False
    

def test_the():
    print("test_the : pass")
    print(str(the))
    return True





