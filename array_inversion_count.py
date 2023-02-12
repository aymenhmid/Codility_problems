#1st method , it works only for small inputs in terms of efficiency , (complexity O(N^2))
def solution(A):
    # Implement your solution here
    if len(A) < 2:
        return 0
    else :
        inv_count = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if (A[i] > A[j]):
                    inv_count += 1
    if inv_count > 10**9:
        return -1
  
    return inv_count
  
  #2nd method , more efficient using mergeSort (complexity O(NlogN))
  def solution(A):
    # Implement your solution here
    def mergeSort(arr,left,right):
        mid = 0
        inv_count = 0
        if(left < right):
            mid = (left + right ) // 2
            inv_count += mergeSort(arr,left,mid)
            inv_count += mergeSort(arr,mid+1,right)
            inv_count += merge(arr,left,mid,right)
        return inv_count
    
    def merge(arr,left,mid,right):
        temp_arr = []
        i = left
        j = mid+1
        inv_count = 0
        while(i<=mid and j<=right):
            if(arr[i] <= arr[j]):
                temp_arr.append(arr[i])
                i+=1
            else:
                temp_arr.append(arr[j])
                inv_count += mid - i + 1
                j+=1
        while(i<=mid):
            temp_arr.append(arr[i])
            i+=1
        while(j<=right):
            temp_arr.append(arr[j])
            j+=1
        for i in range(left,right+1):
            arr[i] = temp_arr[i-left]
        return inv_count
    if len(A) < 2 :
        return 0
    else :
        inv = mergeSort(A,0,len(A)-1)
        if inv > 10**9:
            return -1
        else :
            return inv
