
import random


def mergesort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left_half=mergesort(arr[:mid])
    right_half=mergesort(arr[mid:])

    return merge(left_half,right_half)

def merge(left_half,right_half):
    i=0
    j=0
    res=[]
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            res.append(left_half[i])
            i+=1
        else:
            res.append(right_half[j])
            j+=1
    res.extend(left_half[i:])
    res.extend(right_half[j:])
    return res


arr=[12,3443,54,65,234,45354,32,4]
print(mergesort(arr))

