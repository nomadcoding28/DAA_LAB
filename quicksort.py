def quicksort(arr,low,high):
    if len(arr)<=1:
        return arr
    if low < high:
        pi=partion(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
def partion(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while arr[i] < pivot and i<j:
            i=i+1
        while arr[j] > pivot and i<j:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[j],arr[low]=arr[low],arr[j]
    return j
arr=[10,7,8,9,1,5]
n=len(arr)
print(quicksort(arr,0,n-1))


