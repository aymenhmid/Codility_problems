# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter
def solution(A):
    # Implement your solution here
    
    count = Counter(A) 
    occurences = []
    #print ("count : " ,count)
    d = dict(count)
    #print(d.keys())
    for k in d.keys():
        v = d.get(k)
        if v == 1 :
            occurences.append(k)
    if len(occurences) > 0 :
        return occurences[0]
    else :
        return -1
