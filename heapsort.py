from time import time
from datetime import datetime
def heapify(array, n, i, p):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left][p] > array[largest][p]:
        largest = left

    if right < n and array[right][p] > array[largest][p]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest, p)


def heapsort(array, p):
    starttime = time()
    n = len(array)

    for i in range(n // 2 - 1, - 1, - 1):
        heapify(array, n, i, p)

    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0, p)
    endtime = time()
    finaltime = endtime - starttime
    print(finaltime)

filename = r"C:\411\Sortieralgo\SortBig.txt"
with open(filename, "r") as file:
    data = [line.strip().split(",") for line in file]

for item in data:
    item[5] = datetime.strptime(item[5], "%d.%m.%Y")


p = 2
heapsort(data, p)


p = 4
heapsort(data, p)

p = 5
heapsort(data, p)


p = 6
heapsort(data, p)
