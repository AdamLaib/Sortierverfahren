import time

filename_s = r"C:\M411\Sortierverfahren\SortSmall.txt"
with open(filename_s, "r") as file:
    small = [line.strip().split(",") for line in file]

filename_s = r"C:\M411\Sortierverfahren\SortMedium.txt"
with open(filename_s, "r") as file:
    medium = [line.strip().split(",") for line in file]

filename_s = r"C:\M411\Sortierverfahren\SortBig.txt"
with open(filename_s, "r") as file:
    big = [line.strip().split(",") for line in file]


def time_sort(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    print(end_time - start_time)

def quicksortname(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        same = [x for x in arr[1:] if x[2] == pivot[2]]
        left = [x for x in arr[1:] if x[2] < pivot[2]]
        right = [x for x in arr[1:] if x[2] >= pivot[2]]
        return quicksortname(left) + same + quicksortname(right)


def quicksortplz(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        same = [x for x in arr[1:] if x[4] == pivot[4]]
        left = [x for x in arr[1:] if x[4] < pivot[4]]
        right = [x for x in arr[1:] if x[4] >= pivot[4]]
        return quicksortname(left) + same + quicksortname(right)


def quicksortdate(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        same = [x for x in arr[1:] if x[5] == pivot[5]]
        left = [x for x in arr[1:] if x[5] < pivot[5]]
        right = [x for x in arr[1:] if x[5] >= pivot[5]]
        return quicksortname(left) + same + quicksortname(right)


def quicksortcash(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        same = [x for x in arr[1:] if x[6] == pivot[6]]
        left = [x for x in arr[1:] if x[6] < pivot[6]]
        right = [x for x in arr[1:] if x[6] >= pivot[6]]
        return quicksortname(left) + same + quicksortname(right)

if __name__ == '__main__':
        print(quicksortname(small))

