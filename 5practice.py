import random
import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]


def measure_execution_time(size):
    random_list = generate_random_list(size)
    start_time = time.time()
    merge_sort(random_list)
    end_time = time.time()
    return end_time - start_time


def main():
    sizes = [100, 200, 300, 500, 1000, 2000, 3000, 5000, 6000, 8000, 10000, 50000]
    times = []

    for size in sizes:
        exec_time = measure_execution_time(size)
        times.append(exec_time)
        print(f"Size: {size}, Execution Time: {exec_time:.6f} seconds")

    plt.plot(sizes, times, marker="o", linestyle="-")
    plt.xlabel("n (Number of elements)")
    plt.ylabel("Time (seconds)")
    plt.title("Merge Sort Execution Time")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
