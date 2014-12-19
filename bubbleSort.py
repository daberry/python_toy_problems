def bubbleSort(array):
    done = False
    while not done:
        done = True
        for i in range(0, len(array)):
            if array[i - 1] > array[i]:
                done = False
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temp
    return array
