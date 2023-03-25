#1st solution
def solution(A, K):
    # Implement your solution here
    lst = [0] * len(A)
    if len(A) < 2 or len(A) == K:
        return A
    
    for i in range(len(A)):
        new_index = i+K
        
        if new_index < len(A):
            lst[new_index] = A[i]
        elif new_index >= len(A):
            lst[new_index - len(A)] = A[i]
    return lst
 
#2nd solution
def solution(A, K):
    # Implement your solution here
    if len(A) == 0:
        return A
    for i in range(K):
        last_element = A.pop()
        A.insert(0, last_element)
    
    return A
