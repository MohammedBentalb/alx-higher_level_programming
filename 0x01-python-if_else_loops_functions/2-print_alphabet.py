#!/usr/bin/python3
''' printing the alphabet usig ascii inside the loop'''

for i in range(ord('a'), ord('z') + 1):
   print("{}".format(chr(i)), end = "")
