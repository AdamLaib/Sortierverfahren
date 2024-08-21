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


def insertionsortname(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key[2] < arr[j][2]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    #for row in arr:
        #print(row)

def insertionsortplz(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key[4] < arr[j][4]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    for row in arr:
        print(row)

def insertionsortdate(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key[5] < arr[j][5]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    for row in arr:
        print(row)

def insertionsortcash(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key[6] < arr[j][6]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    for row in arr:
        print(row)

if __name__ == '__main__':
    time_sort(insertionsortname, big)
