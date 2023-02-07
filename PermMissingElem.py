def solution(A):
    # Implement your solution here
    if(len(A) == 0): return 1
    elif(len(A) == 1):
        if(A[0] == 1): return 2
        else: return 1
    else:
        n, sum_val = len(A) + 1, sum(A)
        return int(((n*(n+1)) / 2) - sum_val)
