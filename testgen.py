# Test Bitstream Generator
from bitstream import Bitstream

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

# bs = Bitstream(6, int("000010", 2))
bs = Bitstream(16, 0xaacc)

for (is_lastbit, d) in islast(bs):
    print(f"last: {is_lastbit}  bit: {d}")
