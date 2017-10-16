#!/usr/bin/env python3
# encoding=utf-8
gf = open("gradeslist.txt").read()
glist = list(map(int, gf.split()))
for i in range(5):
    print(i + 1, glist.count(i + 1))
