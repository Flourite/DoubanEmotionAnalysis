# -*- coding: utf-8 -*-
import re
clist = []
glist = []
for i in range(1, 61):
    f1 = open("/Users/liucongyou/Downloads/meirenyu/" + "g" + str(i) + ".txt")
    f2 = open("/Users/liucongyou/Downloads/meirenyu/" + "c" + str(i) + ".txt")
    glist.append([])
    clist.append([])
    for comments in re.findall(r"[\"“](.+?)[\"”]", f1.read()):
        glist[i - 1].append(comments)
    for lines in f2.readlines():
        clist[i - 1].append(lines)
    print(i, len(clist[i - 1]), len(glist[i - 1]),
          len(clist[i - 1]) == len(glist[i - 1]))
