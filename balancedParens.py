def balanced_parens(string):
    stack = []
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for char in string:
        if pairs[char]:
            stack.append(char)
        elif char == '}' or ']' or ')':
            if pairs[stack.pop()] != char:
                return false
    return len(stack) == 0    
