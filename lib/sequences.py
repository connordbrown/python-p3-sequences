#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        fibSeq = []
    elif length == 1:
        fibSeq = [0]
    elif length == 2:
        fibSeq = [0, 1]
    else:
        fibSeq = [0, 1]
        for i in range(length - 2):
            fibSeq.append(fibSeq[i] + fibSeq[i+1])
    print(fibSeq)