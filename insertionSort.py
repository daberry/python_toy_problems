def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        index = i
        while index and value < array[index - 1]:
            array[index] = array[index - 1]
            index -= 1
        array[index] = value
    return array
