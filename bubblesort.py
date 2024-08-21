from time import time
from datetime import datetime
def bubblesortSurname(array):
    start_time = time()
    vorgabe = len(array)
    v = 2
    for i in range(vorgabe):
        for x in range(0, vorgabe-i-1):
            if array[x][v] > array[x+1][v]:
                array[x], array[x+1] = array[x+1], array[x]
    end_time = time()
    timesurn = end_time - start_time
    print(timesurn)
    return array


def bubbleSortDate(array):
    start_time = time()
    n = len(array)
    for i in range(n):
        for x in range(0, n - i - 1):
            date1 = datetime.strptime(data[x][5], "%d.%m.%Y")
            date2 = datetime.strptime(data[x + 1][5], "%d.%m.%Y")
            if date1 > date2:
                array[x], array[x + 1] = array[x + 1], array[x]
    end_time = time()
    timedate = end_time - start_time
    print(timedate)
    return array

def bubblesortPLZ(array):
    start_time = time()
    vorgabe = len(array)
    v = 4
    for i in range(vorgabe):
        for x in range(0, vorgabe -i -1):
            if array[x][v] > array[x+1][v]:
                array[x], array[x+1] = array[x+1], array[x]
    end_time = time()
    timeplz = end_time - start_time
    print(timeplz)
    return array


def bubblesortMoney(array):
    start_time = time()
    vorgabe = len(array)
    v = 6
    for i in range(vorgabe):
        for x in range(0, vorgabe -i -1):
            if array[x][v] > array[x+1][v]:
                array[x], array[x+1] = array[x+1], array[x]
    end_time = time()
    timemoney = end_time - start_time
    print(timemoney)
    return array


filename = r"C:\411\Sortieralgo\SortBig.txt"
with open(filename, "r") as file:
    data = [line.strip().split(",") for line in file]

bubblesortSurname(data)
bubblesortPLZ(data)
bubblesortMoney(data)








