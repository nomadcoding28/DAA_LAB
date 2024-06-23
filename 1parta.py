# import matplotlib.pyplot as plt
# import math
# log_n=lambda x:math.log(x,2)
# n_2=lambda x:x**2
# xpts=[x for x in range(1000,20000,2000)]
# plt.plot(xpts,[log_n(i) for i in xpts],label="log_n")
# plt.plot(xpts,[n_2(i)for i in xpts],label="n_2")
# plt.ylim([0,1000000])
# # ymax = max(max(log_n), max(n_2))
# # plt.ylim([0, ymax * 1.1])
# plt.legend(title="Functions")
# plt.show()

# def binarysearch(arr,low,high,key):
#     if low<high:
#         m=(low+high)//2
#         if arr[m]==key:
#             return m
#         elif arr[m]>key:
#             return binarysearch(arr,low,m-1,key)
#         else:
#             return binarysearch(arr,m+1,high,key)
#     else:
#         return -1
# def linearsearch(arr,key):
#     if len(arr)==0:
#         return -1
#     else:
#         for i in range(len(arr)-1):
#             if arr[i]==key:
#                 return i
#             else:
#                 continue
# arr=[1,2,5,7,12,45,78,89,545,898]
# low=0
# high=len(arr)
# key=5
# key2=545
# print(binarysearch(arr,low,high,key))
# print(linearsearch(arr,key2))
