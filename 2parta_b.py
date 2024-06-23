# import numpy as np
# import matplotlib.pyplot as plt

# def f(n):
#     return 7 * n + 5

# def g(n):
#     return n

# c = 8

# n_values = np.arange(1, 11, 1)

# f_values = f(n_values)
# cg_values = c * g(n_values)

# n0 = np.min(n_values[f_values <= cg_values])

# # Print the n0 value and the values of f(n) and c * g(n)
# print("n0:", n0)
# print("Values of f(n):", f_values)
# print("Values of c * g(n):", cg_values)

# plt.plot(n_values, f_values, label='f(n) = 7n + 5')
# plt.plot(n_values, cg_values, label=f'c * g(n) = {c}n')
# plt.axvline(x=n0, color='r', linestyle='--', label=f'n0 = {n0}')
# plt.xlabel('n')
# plt.ylabel('Value')
# plt.title('Comparison of f(n) and c * g(n)')
# plt.legend()
# plt.grid(True)
# plt.show()


# def selectionsort(arr):
#     for i in range(len(arr)):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[i],arr[min]=arr[min],arr[i]
#     return arr

# arr=[64,25,12,22,11]
# sortedarr=selectionsort(arr)
# print(sortedarr)
