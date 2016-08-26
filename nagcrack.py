#!/usr/bin/python

import argparse, zlib, base64

class color:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Show more output", action="store_true")
parser.add_argument("string", help="String to be decoded")
args = parser.parse_args()
try:
	if args.verbose: print("Decoding string for the first time... "),
	toencode = base64.b64decode(args.string);
	print(color.OK + "done." + color.ENDC)
except:
	print(color.FAIL + "error." + color.ENDC)
try:
	if args.verbose: print("Looping through decompressed stringlist... "),
	for i in range(5):
		toencode = zlib.decompress(toencode)
		toencode = list(toencode)
		toencode.reverse()
		toencode = "".join(toencode)
		toencode = base64.b64decode(toencode)
	print(color.OK + "done." + color.ENDC)
except:
	print(color.FAIL + "error." + color.ENDC)
print
print("Decoded string: " + color.WARNING + toencode + color.ENDC)
print
	
