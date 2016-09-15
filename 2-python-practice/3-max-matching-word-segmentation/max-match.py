# -*- coding: utf-8 -*-
#!/usr/bin/env python
import cPickle as pickle
import sys, traceback

MAXWORDLENGTH = 20

def max_match_segment( line, dic ):
    words = []
    startIndex = 0
    traceIndex = startIndex # 引入变量使得不匹配时单词处理
    while startIndex < len(line):
        endIndex = min(startIndex + MAXWORDLENGTH, len(line))
        while endIndex > startIndex:
            if line[startIndex : endIndex] in dic:
                if traceIndex < startIndex:
                    words.append(line[traceIndex: startIndex])
                words.append(line[startIndex : endIndex])
                startIndex = endIndex
                traceIndex = startIndex
                break
            else:
                endIndex -= 1
                if endIndex == startIndex:
                    # 不匹配
                    startIndex += 1
                    break


    return words


if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[2]))
    except:
        print >> sys.stderr, "failed to load dict"
        traceback.print_exc()
        sys.exit(1)

    for line in fpi:
        print " ".join( max_match_segment(line.strip(), dic) )

