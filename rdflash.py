# Python script to upload a binary file from the XuLA FPGA.

import sys
import time

from xula import XuLA, elapsed, UnknownDevice
# from bitstream import Bitstream, BitstreamHex, BitFile

def main(bitfilename, loaddr, hiaddr):
    x = XuLA()
    chain = x.querychain()
    if chain != [0x02218093]:
       print(f"Expected single XC3S200A, but chain is {chain}")
       raise UnknownDevice("Invalid device: " + hex(chain[0]))

    print("OK, found DEVICEID for XC3S200A")
    t = time.time()
    x.read_flash(bitfilename, loaddr, hiaddr, True)
    t = time.time() - t
    print(f"read complete, took {elapsed(t)}")

def convert(x):
    if x.startswith('0x') or x.startswith('0X'):
        return int(x, 16)
    return int(x)

if __name__ == "__main__":
    print("XuLA Flash uploader")
    if len(sys.argv) != 4:
        print(f"usage: python {sys.argv[0]} <bitfile> <loaddr> <hiaddr>")
        sys.exit(1)
    
    try:
        loaddr = convert(sys.argv[2])
        hiaddr = convert(sys.argv[3])
        main(sys.argv[1], loaddr, hiaddr)
        sys.exit(0)

    except ValueError:
        print('Invalid arguments for low or high address')
        sys.exit(1)

    except UnknownDevice as X:
        print(X)
        sys.exit(1)
