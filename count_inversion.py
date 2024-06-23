def mergesort(arr):
    if len(arr)<=1:
        return arr,0
    mid=len(arr)//2
    left_half, left_inv=mergesort(arr[:mid])
    right_half, right_inv=mergesort(arr[mid:])
    merged, merged_inv=merge(left_half, right_half)
    total_inv=left_inv+merged_inv+right_inv
    return merged,total_inv
def merge(left_half,right_half):
    i=0
    j=0
    inv_count=0
    res=[]
    while i<len(left_half) and j<len(right_half):
        if left_half[i]<=right_half[j]:
            res.append(left_half[i])
            i+=1
        else:
            res.append(right_half[j])
            j+=1
            inv_count+=len(left_half)-i
    res.extend(left_half[i:])
    res.extend(right_half[j:])
    return res,inv_count
arr = [12, 11, 13, 5, 6, 7]
sorted_arr, inversions = mergesort(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)