#!/usr/bin/env python3
# encoding=utf-8
import nltk
import random
cf = open("bigramcommentslist.txt").readlines()
clist = []
for lines in cf:
    clist.append(lines.split())

gf = open("gradeslist.txt").read()
glist = map(int, gf.split())

wordfreq = dict()
for comments in clist:
    for word in comments:
        wordfreq[word] = wordfreq.get(word, 0) + 1

worddict = dict()
i = 0
for word in (word for word in wordfreq.keys() if wordfreq[word] > 1):
    worddict[word] = i
    i = i + 1

dataset = []
for (sepcom, grade) in zip(clist, glist):
    comment = set(sepcom)
    features = {}
    for word in worddict:
        if word in comment:
            features[word] = sepcom.count(word)
    dataset.append((features, grade))

test_scale = 0.2
ilist = random.sample(range(len(dataset)), int(len(dataset) * 0.2))
trainset = []
testset = []
for i in range(len(dataset)):
    if i in ilist:
        testset.append(dataset[i])
    else:
        trainset.append(dataset[i])

classifier = nltk.NaiveBayesClassifier.train(trainset)
total = 0
accurate = 0

for (features, grade) in testset:
    test = classifier.classify(features)
    total += 1
    if test == grade:
        accurate += 1

print("%d/%d, %.2f%%" % (accurate, total, float(accurate) / float(total) * 100))
