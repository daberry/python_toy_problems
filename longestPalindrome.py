def longestPalindrome(string):
    length = len(string)
    result = ""
    def recurse(left, right):
        while left >= 0 and right < length and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]
    for i in range(0, length):
        oddPal = recurse(i - 1, i + 1)
        evenPal = recurse(i, i + 1)
        if len(oddPal) > len(result):
            result = oddPal
        if len(evenPal) > len(result):
            result = evenPal
    return result
