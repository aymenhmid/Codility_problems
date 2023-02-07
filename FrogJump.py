# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    M  = (Y - X) % D
    #print('M : ',M)
    if (M == 0):
        return (Y - X) // D
    else :
        return ((Y - X) // D) + 1
