from Num import Num
from Sym import Sym
from Start import the
import Query
from Data import *
import Misc
from pathlib import Path
import os , csv
import Update
import Cluster, Discretization
import Optimize as optimize

def test_nums():
    val = Num()
    val1 = Num()
    for i in range(1000):
        val.add(Misc.rand())
    for i in range(1000):
        val1.add(Misc.rand()**2)
    print("Test num : successful \n")
    print(1,Misc.rnd(val.mid()), Misc.rnd(val.div()))
    print(2,Misc.rnd(val1.mid()), Misc.rnd(val1.div())) 
    return .578 == Misc.rnd(val.mid()) and val.mid()> val1.mid() 


def test_sym():
    value = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    sym1 = Sym()
    for x in value:
        sym1.add(x)
    if("a"==sym1.mid() and 1.379 == Misc.rnd(sym1.div())):
        print(" Test sym : successful \n")
    return "a"==sym1.mid() and 1.379 == Misc.rnd(sym1.div())

def readCSV(sFilename, fun):
  
    with open(sFilename, mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            fun(line)


def test_csv():

    global n
    def fun(t):
        n += len(t)
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    if(csv_content(csv_path) == 8 * 399):
        print(" Test csv : successful \n")
    return csv_content(csv_path) == 8 * 399

def csv_content(src):
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        l =0
        for row in csvFile:
            l += len(row)
        return l


def test_data():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read_file(csv_path)
    col = data.cols.x[1].col
    print("Test data : successful \n")
    print(col.lo,col.hi, Query.mid(col), Query.div(col))
    print(Query.stats(data))
    return True



def test_clone():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data = Data()
    data1 = data.read_file(csv_path)
    data2 = data1.clone(data1,data1.rows)
    print("Test clone : successful \n")
    Misc.oo(Query.stats(data1))
    Misc.oo(Query.stats(data2))
    return True

def test_the():
    print("Test the : successful")
    print(str(the))
    return True

def test_half():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()
    data = data1.read_file(csv_path)

    left, right, A, B, c = Cluster.half(data)
    print("Test half : successful \n")
    print(len(left), len(right), len(data.rows))
    print(Misc.o(A), c)
    print(Misc.o(B))
    return True

def test_cliffs():
    if Misc.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [8, 7, 6, 2, 5, 8, 7, 3]):
        return False
    if not Misc.cliffs_delta([8, 7, 6, 2, 5, 8, 7, 3], [9, 9, 7, 8, 10, 9, 6]):
        return False

    t1, t2 = [], []
    for i in range(1000):
        t1.append(Misc.rand())
        t2.append(math.sqrt(Misc.rand()))
    if Misc.cliffs_delta(t1, t1):
        return False
    if not Misc.cliffs_delta(t1, t2):
        return False
    diff, j = False, 1.0
    while not diff:
        t3 = list(map(lambda x: x * j,t1))
        diff = Misc.cliffs_delta(t1, t3)
        print(">", Misc.rnd(j), diff)
        j *= 1.025
    print("Test cliff : successful \n")
    return True

def test_dist():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read_file(csv_path)
    num = Num()
    for row in data.rows:
        Update.add(num, Query.dist(data, row, data.rows[1]))
    print("Test dist : successful \n")
    print({"lo": num.lo, "hi": num.hi, "mid": Misc.rnd(Query.mid(num)), "div": Misc.rnd(num.n)})
    return True

def test_tree():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read_file(csv_path)
    print("Test tree : successful \n")
    Cluster.show_tree(Cluster.tree(data))

    return True


def test_sway():
  
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()
    data = data1.read_file(csv_path)
    best, rest = optimize.sway(data)
    print(Misc.o(Query.stats(data)))
    print("\nall ", Misc.o(Query.stats(data)))
    print("    ",  Misc.o( Query.stats(data, Query.div)))
    print("\nbest", Misc.o(Query.stats(best)))
    print("    ",   Misc.o(Query.stats(best, Query.div)))
    print("\nrest", Misc.o(Query.stats(rest)))
    print("    ",   Misc.o(Query.stats(rest, Query.div)))
    print("\nall ~= best?", Misc.o(Misc.diffs(best.cols.y, data.cols.y)))
    print("best ~= rest?", Misc.o(Misc.diffs(best.cols.y, rest.cols.y)))
    return True



def test_bins():
    root = str(Path(__file__).parent.parent.parent)
    csv_path = os.path.join(root, "etc/data/auto93.csv")
    data1 = Data()

    data = data1.read_file(csv_path)
    best, rest = optimize.sway(data)
    print("Test bin : successful")
    print("all","","","",Misc.o({"best":len(best.rows), "rest": len(rest.rows)}))
    for k,t in enumerate(Discretization.bins(data.cols.x, {"best": best.rows, "rest": rest.rows})):
        for _, range in enumerate(t):
            print(range.txt, range.lo, range.hi,round(Query.value(range.y.has, len(best.rows), len(rest.rows), "best")),
                  range.y.has)
    print("end")
    return  True 
