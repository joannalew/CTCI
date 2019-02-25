# Binary Heap Implementation in Python
# Ref: http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapImplementation.html

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def bubbleUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList = tmp
            i = i // 2
    
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.bubbleUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def sinkDown(self, i):
        while (i * 2) <= self.currentSize:
            minIndex = self.minChild(i)
            if self.heapList[i] > self.heapList[minIndex]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minIndex]
                self.heapList[minIndex] = tmp
            i = minIndex
    
    def delMin(self):
        returnValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.sinkDown(1)
        return returnValue

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.sinkDown(i)
            i -= 1

def main():
    heap = BinHeap()
    heap.buildHeap([7, 10, 20, 3, 4, 49, 50])
    print(heap.heapList)
    print('--------------------')
    heap.buildHeap([33, 14, 17, 27, 18, 19, 9, 21, 5, 11])
    print(heap.heapList)
    heap.insert(7)
    print(heap.heapList)

if __name__ == "__main__":
    main()
    