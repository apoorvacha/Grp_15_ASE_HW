import List, Query
from Start import the
from Cluster import half



def sway(data):
      def worker(rows, worse, evals0, above = None):
        if len(rows) <= len(data.rows)**(0.5):
            return rows, List.many(worse, the["rest"] * len(rows)), evals0
        else:
            l , r, A, B,c, evals = half(data, rows, None,  above)
            if Query.better(data, B, A):
                l, r, A, B = r, l, B, A
            for row in r:
                worse.append(row)
            return worker(l, worse,evals+evals0, A)

      best, rest , evals = worker(data.rows, [], 0)
      return data.clone(data, best), data.clone(data, rest), evals

