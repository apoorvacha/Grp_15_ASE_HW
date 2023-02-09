from Misc import *
from Cols import *
from Row import *
import math, csv
from typing import List

def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = list(csv.reader(file))
        res.append(csvFile)

    return res

class Data:
    def __init__(self,src):
        self.rows = []
        self.cols = None

        if type(src) == str:
            csv_list = csv_content(src)
            for content in csv_list:
                for row in content:
                    row_cont = []
                    for val in row:
                        row_cont.append(val.strip())
                    self.add(row_cont)

        elif type(src) == List[str]:
            self.add(src)


    def add(self,t:list[str]):

        if (self.cols):
            row = Row(t)
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols = Cols(t)


    def clone(self,init= []):
        data = Data({self.Cols.names})
        return data


    def stats(self, what, cols: Cols, n_places):
        def fun(k, col):
            return col.rnd(getmetatable(col, what), n_places), col.txt
        # return Misc.kap(cols, fun)
        return kap(cols, fun)


    def dist(self, row1, row2, cols, n, d):
        n, d = 0, 0
        for _, col in enumerate(cols or self.cols.x):
            n = n + 1
            d = d + col.dist(row1[col.at], row2[col.at]) ** 2
        return (d / n) ** (1 / 2)


    def around(self, row1, rows = None , cols= None):
        if not rows:
            rows = self.rows
        def fun(row2):
            return {"row": row2, "dist": self.dist(row1, row2, cols)}
        u = map(fun,rows)
        return sorted(u,key = lambda x: x['dist'])

    def furthest(self, row1, rows, cols, t):
        t = self.around(row1, rows, cols)
        return t[-1]

    def half(self, rows, cols, above):
        pass 

    def cluster(self, rows=None, min_size=None, cols=None, above=None):
        pass

