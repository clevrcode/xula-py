# Python script to store a .BIT file in the XuLA Flash.

import sys
import time

from xula import XuLA, elapsed, UnknownDevice
from bitstream import BitFile

def main(bitfilename):
    x = XuLA()
    chain = x.querychain()
    if chain != [0x02218093]:
       print(f"Expected single XC3S200A, but chain is {chain}")
       raise UnknownDevice("Invalid device: " + hex(chain[0]))

    print("OK, found DEVICEID for XC3S200A")
    t = time.time()
    x.write_flash(BitFile(bitfilename), 0, True)
    t = time.time() - t
    print(f"download complete, took {elapsed(t)}")

if __name__ == "__main__":
    print("XuLA Flash downloader")
    if len(sys.argv) != 2:
        print(f"usage: python {sys.argv[0]} <bitfile>")
        sys.exit(1)
    try:
        main(sys.argv[1])
        sys.exit(0)
    except Exception as X:
        print(X)
        sys.exit(1)
