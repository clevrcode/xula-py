# Test Bitstream Generator

class Bitstream:
    """
    Simple bitstream specified as a count and integer value.
    """
    def __init__(self, n, val):
        self.n = n
        self.val = val

    def __iter__(self):
        def getbits():
            for i in range(self.n):
                yield (self.val >> i) & 1
        return getbits()

    def __len__(self):
        return self.n


def islast(o):
    it = o.__iter__()
    e = next(it)
    while True:
        try:
            nxt = next(it)
            yield (False, e)
            e = nxt
        except StopIteration:
            yield (True, e)
            break


USER1 = Bitstream(6, int("000010", 2))

bs = USER1
for (is_lastbit, d) in islast(bs):
    print(f"last: {is_lastbit}  bit: {d}")
