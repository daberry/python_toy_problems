# A basic implementation
def quickSort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x = pivot:
                equal.append(x)
            else:
                greater.append(x)
    quickSort(less)
    quickSort(equal)
    quickSort(greater)
    array = less + equal + greater

# A better implementation that works in place, 
# without needing to allocate additional space
def quickSort(array):
    if len(array) > 1:
        pivot = array[len(array) / 2]
        left = 0
        right = len(array) - 1
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    quickSort(array[0:right])
    quickSort(array[right + 1:])
