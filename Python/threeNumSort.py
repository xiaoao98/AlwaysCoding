from collections import deque
import heapq

def threeNumberSort(array, order):
    firstEle = order[0]
    lastEle = order[-1]
    size = len(array)
    firstIndex = -1
    lastIndex = size
    i = 0
    while i < lastIndex:
        if array[i] == lastEle:
            lastIndex -= 1
            swap(array, lastIndex, i)
        if array[i] == firstEle:
            firstIndex += 1
            swap(array, firstIndex, i)
            i += 1
        else:
            i += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    # array = [1, 0, 0, -1, -1, 0, 1, 1]
    # order = [0, 1, -1]
    # print(threeNumberSort(array, order))
    que = deque([])
    print(len(que))
    que.append(3)
    que.append(5)
    que.append(7)
    print(len(que))
    print(que[1])
    for i in range(len(que)):
        print(que.popleft())
    a = [3, 5, 1, 3, 5, 2, 10, 4, 7]
    heapq.heapify(a)
    heapq.heappush(a, 9)
    print(heapq.heappop(a))
    print(heapq.nlargest(3, a))
    print(heapq.nsmallest(3, a))


