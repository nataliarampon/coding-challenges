# Use of stdin cause it's faster than input() and it was giving me a time limit error
from sys import stdin

def merge(list, merged_list, left_pointer, mid_pointer, end_pointer):
    swaps = 0
    i = k = left_pointer
    j = mid_pointer + 1

    while i <= mid_pointer or j <= end_pointer:
        if i > mid_pointer:
            merged_list[k] = list[j]
            j += 1
        elif j > end_pointer:
            merged_list[k] = list[i]
            i += 1
        elif list[i] > list[j]:
            swaps += (mid_pointer - i) + 1
            merged_list[k] = list[j]
            j += 1
        else:
            merged_list[k] = list[i]
            i += 1
        k += 1
    for i in range(left_pointer, end_pointer+1):
        list[i] = merged_list[i]
    return swaps

def mergeSort(list, merged_list, left_pointer, right_pointer):
    swaps = 0
    if left_pointer < right_pointer:
        mid_pointer = (left_pointer + right_pointer) // 2
        swaps += mergeSort(list, merged_list, left_pointer, mid_pointer)
        swaps += mergeSort(list, merged_list, mid_pointer + 1, right_pointer)
        swaps += merge(list, merged_list, left_pointer, mid_pointer, right_pointer)
    return swaps

def main():
    for _ in range(int(stdin.readline())):
        size = int(stdin.readline())
        wagons = list(map(int, stdin.readline().split()))
        merged = [0] * size
        swaps = mergeSort(wagons, merged, 0, size - 1)
        print(f'Optimal train swapping takes {swaps} swaps.')

if __name__ == "__main__":
    main()