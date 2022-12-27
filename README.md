# xula-py

Xula tools for python 3.x

# Notes on porting XSTools.

1- First, install the USB driver for xula with the zadig utility.
This tool setup the driver for libusb0. So trying to use libusb-1.0.dll
fails. Crashes in call to WaitForMultipleObject.
Using libusb0.dll works OK.
IMPORTANT: Must use libusb0.dll backend

2- Changed all 'print xxx' to 'print(xxx)'

3- Changed the bytes function to mkbytes because it cause confusion with the
bytes object constructor.

4- Change .tostring() to .tobytes() for Bitstream objects.

5- In jtag.py, changed it.next() to it.**next**(). Could have changed to next(it).

6- In rdflash.py, added validation of address values arguments. Also added option to
specify hex values by prefixing with '0x' or '0X'.

7- Added tqdm progress bar to the write_flash() method in xula.py.

8- Added new method (enableflash()) to enable FPGA configuration from flash.
This method sets the FLASH_ENABLE_FLAG_ADDR of the PIC uC EEPROM so that
the FPGA auto configures itself from the flash memory at powerup.
The method can also clear this flag to resume config from the JTAG download.

NOTE: To allow for flash configuration, the bitstream dowloaded to the flash Must
be configured with startup clock set to CCLK.
