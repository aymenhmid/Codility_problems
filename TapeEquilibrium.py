def solution(A):
    # Implement your solution here
    if len(A) < 2 :
        return 0
    else :
        minDiff = 5000
        S = sum(A)
        SL = 0
    
        for i in range(0,len(A) -1):
            SL += A[i]
            diff = abs(2*SL - S)
            minDiff = min((minDiff,diff))
    return minDiff
