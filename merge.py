# Given two sorted integer arrays A and B, merge B into A as one sorted arrays

class Solution(object):
    # @param A: a list of integers
    # @param m: an integer, length of A
    # @param B: a list of integers
    # @param n: an integer, length of B
    def merge(self, A, m, B, n):
        while n > 0:
            if m > 0 and A[m-1] > B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1
