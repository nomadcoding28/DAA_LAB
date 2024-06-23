# import random
# import time
# import matplotlib.pyplot as plt

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# def generate_random_list(size):
#     return [random.randint(1, 10000) for _ in range(size)]

# def measure_execution_time(size):
#     random_list = generate_random_list(size)
#     start_time = time.time()
#     merge_sort(random_list)
#     end_time = time.time()
#     return end_time - start_time

# def main():
#     sizes = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 6000, 8000, 10000, 50000]
#     times = []

#     for size in sizes:
#         exec_time = measure_execution_time(size)
#         times.append(exec_time)
#         print(f"Size: {size}, Execution Time: {exec_time:.6f} seconds")

#     plt.plot(sizes, times, marker='o', linestyle='-')
#     plt.xlabel('n (Number of elements)')
#     plt.ylabel('Time (seconds)')
#     plt.title('Merge Sort Execution Time')
#     plt.grid(True)
#     plt.show()

# if __name__ == "__main__":
#     main()

# def merge_and_count(arr, left, mid, right):
#     left_half = arr[left:mid + 1]
#     right_half = arr[mid + 1:right + 1]

#     i = j = 0
#     k = left
#     inv_count = 0

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] <= right_half[j]:
#             arr[k] = left_half[i]
#             i += 1
#         else:
#             arr[k] = right_half[j]
#             inv_count += (mid - i + 1 - left)
#             j += 1
#         k += 1

#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i += 1
#         k += 1

#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j += 1
#         k += 1

#     return inv_count

# def merge_sort_and_count(arr, left, right):
#     inv_count = 0
#     if left < right:
#         mid = (left + right) // 2

#         inv_count += merge_sort_and_count(arr, left, mid)
#         inv_count += merge_sort_and_count(arr, mid + 1, right)
#         inv_count += merge_and_count(arr, left, mid, right)

#     return inv_count

# def count_inversions(arr):
#     return merge_sort_and_count(arr, 0, len(arr) - 1)

# def recommend_playlist(user_playlists):
#     num_users = len(user_playlists)
#     recommendations = []

#     for i in range(num_users):
#         min_inversions = float('inf')
#         best_playlist = None

#         for j in range(num_users):
#             if i != j:
#                 current_inversions = count_inversions(user_playlists[i][:])
#                 if current_inversions < min_inversions:
#                     min_inversions = current_inversions
#                     best_playlist = user_playlists[j]

#         recommendations.append(best_playlist)

#     return recommendations

# # Example usage:
# user_playlists = [
#     [3, 1, 2, 5, 4, 8, 6, 7],
#     [4, 3, 1, 2, 8, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7, 8]
# ]

# recommendations = recommend_playlist(user_playlists)
# for i, recommendation in enumerate(recommendations):
#     print(f"Recommendation for User {i + 1}: {recommendation}")
