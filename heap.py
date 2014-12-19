class MaxHeap(object):
    def __init__(self, array):
        self.heap = self.heapify(array)

    def __len__(self):
        return len(self.heap)

    def heapify(self, array):
        length = len(array)
        start = (length - 2) / 2
        while start >= 0:
            self.sift_down(array, start, length-1)
            start -= 1

    def sift_down(self, array, start, end):
        root = start
        while (root * 2 - 1) <= end:
            child = root * 2 - 1
            swap = root

            if array[swap] < array[child]:
                swap = child
            if child + 1 <= end and array[swap] < array[child+1]:
                swap = child + 1
            if swap != root:
                array[root], array[swap] = array[swap], array[root]
                root = swap
            else: 
                return

def heap_sort(array):
    length = len(array)
    end = lenth - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        MaxHeap.sift_down(array, 0, end)

