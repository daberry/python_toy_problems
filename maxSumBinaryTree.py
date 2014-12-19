class Solution:
    def maxSumPath(self, root):
        if not root:
            return 0
        Solution.max = -1000000
        self.maxSum(root)
        return Solution.max

    def maxSum(self, root):
        sum = root.val
        leftMax = 0
        rightMax = 0
        if root.left:
            leftMax = self.maxSum(root.left)
        if root.right:
            rightMax = self.maxSum(root.right)
        if leftMax > 0:
            sum += leftMax
        if rightMax > 0:
            sum += rightMax
        Solution.max = max(Solution.max, sum)
        return max(root.val, max(root.val + leftMax, root.val + rightMax))
