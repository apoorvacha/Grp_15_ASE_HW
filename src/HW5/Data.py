import Misc
from Cols import COLS
import Rows, Examples
import csv, Update, math
# from typing import List, Union


def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            res.append(row)
    return res



class Data:

    def __init__(self):
        self.cols = None
        self.rows = []


    def read_file(self, content):
        data = Data()
        callback_function = lambda t: Update.row(data, t)
        Examples.readCSV(content, callback_function)
        return data

    def clone(self, data, ts=None):
        data1 = Update.row(Data(), data.cols.names)
        for t in ts or []:
            Update.row(data1, t)
        return data1

