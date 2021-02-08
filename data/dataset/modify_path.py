import pathlib
import os
import sys

fname = sys.argv[1]
to_add = sys.argv[2]
to_rem = int(sys.argv[3])

with open(fname) as f:
	lines = f.readlines()

writer = open("new_"+fname,"w")
for line in lines:
	splited = line.split(" ")
	path = splited[0]
	path = to_add + path[to_rem:]
	splited[0] = path

	string = " ".join(splited)
	string = string.strip()
	writer.write(string+"\n")
writer.close()