class Rule:
    def __init__(self, ranges=None, max_size=0):
        self.t = {}
        for range in ranges:
            self.t[range.txt] = self.t[range.txt] if range.txt in t else []
            self.t[range.txt].append({"lo": range.lo, "hi": range.hi, "at": range.at})
        self.prune(self.t, max_size)

    def prune(self, rule, max_size):
        n = 0
        for txt, ranges in enumerate(rule):
            n += 1
            if len(ranges) == max_size[txt]:
                n += 1
                rule[txt] = None
        if n > 0:
            return rule