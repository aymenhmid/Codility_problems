# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    if len(S) == 1:
        return 0
    elif len(S) % 2  == 0:
        return -1
    else :
        j = len(S) // 2
        s1 = S[:j]
        s2 = S[j+1:]
        #print('s1 : ',s1)
        #print('s2 : ',s2)
        ch = s1[::-1]
        #print('ch : ',ch)
        if ch == s2:
            return j
        else :
            return -1
