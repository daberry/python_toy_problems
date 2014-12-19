# Given a triangle, find the min path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# Example:
# [
#       [2],
#     [3, 4],
#    [6, 5, 7],
#   [4, 1, 8, 3]
# ]

# The min path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1)

class Solution(object):

    def minimumTotal(self, triangle):
        result = []
        tier = len(triangle) - 1
        while tier >= 0:
            result.append(self.minOfArray(triangle[tier]))
            tier -= 1
        return sum(result)

    def minOfArray(self, array):
        minimum = [array[0]]
        for element in array[1:]:
            if element < minimum[0]:
                minimum[0] = element
        return minimum[0]
