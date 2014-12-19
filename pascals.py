class Solution(object):
    def pascals(self, numRows):
        result = []
        if numRows == 0: return result
        current = []
        for i in range(1, numRows+1):
            current = [1 for val in range(i)]
            if i > 2:
                for j in range(0, i-1):
                    current[j] = result[i-2][j-1] + result[i-2][j]
            result.append(current)
        return result
