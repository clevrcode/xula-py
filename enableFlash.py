import sys
import time

from xula import XuLA, elapsed, UnknownDevice

def main(enableFlash):
    x = XuLA()
    chain = x.querychain()
    if chain != [0x02218093]:
       print(f"Expected single XC3S200A, but chain is {hex(chain[0])}")
       raise UnknownDevice("Invalid device: " + hex(chain[0]))

    print("OK, found DEVICEID for XC3S200A")
    t = time.time()
    x.enableflash(enableFlash)
    t = time.time() - t
    print(f"Configuration change complete, took {elapsed(t)}")

if __name__ == "__main__":
    enableFlash = False
    print("XuLA Flash Enable/Disable")
    if len(sys.argv) != 2:
        print(f"usage: python {sys.argv[0]} [<enableFlash T|F> default False]")
        sys.exit(1)

    enableFlash = sys.argv[1].startswith('t') or sys.argv[1].startswith('T')
    try:
        main(enableFlash)
        sys.exit(0)

    except Exception as X:
        print(X)
        sys.exit(1)

