#!/usr/bin/env python3
# encoding=utf-8
cf = open("commentslist.txt").readlines()
clist = []
for lines in cf:
    clist.append(lines.split())

gf = open("gradeslist.txt").read()
glist = gf.split()

wordfreq = dict()
for comments in clist:
    for word in comments:
        wordfreq[word] = wordfreq.get(word, 0) + 1

worddict = dict()
i = 0
for word in (word for word in wordfreq.keys() if wordfreq[word] > 1):
    worddict[word] = i
    i = i + 1

svmfile = open("svm.txt", "w")
for g, c in zip(glist, clist):
    svmfile.write(str(g) + " ")
    cdict = dict()
    for word in worddict.keys():
        if word in c:
            cdict[worddict[word]] = c.count(word)
    for (word, freq) in cdict.items():
        svmfile.write(str(word) + ":" + str(freq) + " ")
    svmfile.write("\n")
svmfile.close()
