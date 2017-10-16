#!/usr/bin/env python3
# encoding=utf-8
import jieba
import re
movies = 60
clist = []
glist = []
gradedict = {'较差': 2, '很差': 1, '力荐': 5, '还行': 3, '推荐': 4}
stopwords = ["\n", "。", "、", "，", "…", " ", "！", "？", "的"]
for i in range(movies):
    cf = open("c" + str(i + 1) + ".txt")
    gf = open("g" + str(i + 1) + ".txt")
    for lines in cf.readlines():
        sepcom = jieba.lcut(lines)
        for stpwd in stopwords:
            for word in sepcom[:]:
                if word == stpwd:
                    sepcom.remove(word)
        clist.append(sepcom)
    for comments in re.findall(r"[\"“](.+?)[\"”]", gf.read()):
        glist.append(gradedict[comments])

cf = open("commentslist1.txt", "w")
gf = open("gradeslist1.txt", "w")
for comments in clist:
    cf.write(" ".join(comments) + "\n")
for grade in glist:
    gf.write(str(grade) + "\n")
cf.close()
gf.close()
