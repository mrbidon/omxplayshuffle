# -*- coding: utf8
import sys
path = "/usr/local/lib/python2.7/dist-packages/omxplayshuffle-0.5.0.6-py2.7.egg"
if path in sys.path  :
    sys.path.remove(path)
sys.path.append("../")


from  omxplayshuffle.main import get_files_list

import random
import numpy

nb_iter = 100000

def get_score(nom_et_score):
     return nom_et_score[1]

def main():
    print("path {0}".format(sys.argv[1])    )
    orig_list = get_files_list(sys.argv[1])
    scores = {}
    for item in orig_list :
        scores[item] = 0

    for iter in range(0,nb_iter):
        new_list = orig_list
        random.shuffle(new_list, numpy.random.uniform)
        for i in range(0, 10):
            scores[new_list[i]] += 1

    result = sorted(scores.items(), key=get_score)

    for line in result :
        print("{0} : {1}").format(line[0][0:10],line[1])

if __name__ == '__main__':
    main()
