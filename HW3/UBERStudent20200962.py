#!/usr/bin/python3
from datetime import datetime, date
import sys

daylist = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
dic1 = dict()
dic2 = dict()

with open(sys.argv[1], "rt") as rf:
	for line in rf:
		uber = line.split(",")
		uber[-1] = uber[-1].split("\n")[0]
		day = uber[1].split("/")
		uber[1] = daylist[date(int(day[2]), int(day[0]), int(day[1])).weekday()]

		key = uber[0] + "," + uber[1]
		if key not in dic1:
			dic1[key] = int(uber[2])
			dic2[key] = int(uber[3])
		else:
			dic1[key] += int(uber[2])
			dic2[key] += int(uber[3])

keylist = dic1.keys()
with open(sys.argv[2], "wt") as wf:
	for key in keylist:
		wf.write(key)
		wf.write(" ")
		wf.write(str(dic1[key]))
		wf.write(",")
		wf.write(str(dic2[key]))
		wf.write("\n")
