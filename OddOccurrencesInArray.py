from collections import Counter
def solution(A):
    # Implement your solution here
    counts = Counter(A)
    
    for key, value in counts.items():
        x = counts[key]
        if x % 2 != 0:
            return key
