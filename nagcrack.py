#!/usr/bin/python

import argparse
import zlib
import base64
import binascii


class Color:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Show more output", action="store_true")
parser.add_argument("string", help="String to be decoded")
args = parser.parse_args()
todecode = ''
try:
    if args.verbose: print("Decoding string for the first time... "),
    todecode = base64.b64decode(args.string)
    print(Color.OK + "done." + Color.ENDC)
except binascii.Error:
    print(Color.FAIL + "error.")
    print("No correct base64-encoded string defined." + Color.ENDC)
if args.verbose: print("Looping through decompressed stringlist... "),
for i in range(5):
    todecode = zlib.decompress(todecode)
    todecode = list(todecode)
    todecode.reverse()
    todecode = "".join(todecode)
    todecode = base64.b64decode(todecode)
print(Color.OK + "done." + Color.ENDC)
print("\nDecoded string: " + Color.WARNING + todecode + Color.ENDC + "\n")
