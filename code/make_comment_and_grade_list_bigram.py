#!/usr/bin/env python3
# encoding=utf-8
f = open("commentslist.txt").readlines()
glist = []
for lines in f:
    sep = lines.split()
    ext = []
    for i in range(len(sep) - 1):
        ext.append(sep[i] + sep[i + 1])
    glist.append(sep + ext)
f = open("bigramcommentslist1.txt", "w")
for lines in glist:
    f.write(" ".join(lines) + "\n")
