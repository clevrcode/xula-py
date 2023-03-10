# Python script to download a bitstream into the XuLA FPGA
# File originally from http://excamera.com/sphinx/fpga-xess-python.html
# Minor changes by Hector Peraza.

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
    x.progpin(1)
    x.progpin(0)
    x.progpin(1)
    time.sleep(0.03)
    x.load(BitFile(bitfilename))
    t = time.time() - t
    print(f"load complete, took {elapsed(t)} USERCODE = {hex(x.usercode())}")

if __name__ == "__main__":
    print("XuLA FPGA loader")
    if len(sys.argv) != 2:
        print(f"usage: python {sys.argv[0]} <bitfile>")
        sys.exit(1)

    try:
        main(sys.argv[1])
        sys.exit(0)
    except Exception as X:
        print(X)
        sys.exit(1)

