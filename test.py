# import os
# os.environ['PYUSB_DEBUG'] = 'debug'
# os.environ['LIBUSB_DEBUG'] = '4'

# from tqdm import tqdm
from time import sleep

import usb.core
import usb.util

from xula import XuLA
x = XuLA()
print(x)

# pbar = tqdm(total=100)
# for i in range(10):
#     sleep(0.1)
#     pbar.update(10)
# pbar.close()


# dev = usb.core.find(idVendor=0x8087, idProduct=0x0026)
# dev = usb.core.find(idVendor=0x04d8, idProduct=0xff8c)
# print(dev)
