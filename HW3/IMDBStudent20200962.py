#!/usr/bin/python3
import sys

dic = dict()

with open(sys.argv[1], "rt") as rf:
	for line in rf:
		genre = line.split("::")[2].split("|")
		genre[-1] = genre[-1].split("\n")[0]
		print(genre)
		for g in genre:
			if g not in dic:
				dic[g] = 1
			else:
				dic[g] += 1

keylist = dic.keys()
with open(sys.argv[2], "wt") as wf:
	for key in keylist:
		wf.write(key)
		wf.write(" ")
		wf.write(str(dic[key]))
		wf.write("\n")
