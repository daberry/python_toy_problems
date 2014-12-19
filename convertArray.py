# 2. Given an array [a_1, a_2, ..., a_N, b_1, b_2, ..., b_N, c_1, c_2, ..., c_N],
#    efficiently convert it to 
#    [a_1, b_1, c_1, a_2, b_2, c_2, ..., a_N, b_N, c_N]
#    using as little space as possible.

# The element at the ith position in the final array
# is at position (i % 3) * N + (i / 3) in the original array

# Solution that breaks the constant space constraint
def getIndex(currentIndex, N):
    return (currentIndex % 3) * N + (currentIndex / 3)

def convertArrayWithExtraSpace(array):
    N = len(array)
    return [array[getIndex(i, N)] for i in range(len(array))]

def convertArray(array):
    N = len(array) / 3
    for currentIndex in range(len(array)):
        swapIndex = getIndex(currentIndex, N)
        while swapIndex < currentIndex:
            swapIndex = getIndex(swapIndex, N)
        array[currentIndex], array[swapIndex] = array[swapIndex], array[currentIndex]
