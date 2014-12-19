def mergeSort(array):
    if len(array) == 1:
        return array
    middle = len(array) / 2
    left = array[0:middle]
    right = array[middle + 1:]
    left = mergeSort(left)
    right = mergeSort(right)
    return [merge(left, right)]

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    if left:
        result + left[leftIndex:]
