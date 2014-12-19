# Given a string and a pattern, write a function to determine if
# the string matches the pattern.

def matchPattern(pattern, string):
    if len(string) == 0:
        return len(pattern) == 0 or pattern[0] == '*'
    if len(pattern) == 0:
        return len(string) == 0

    curr_reg = pattern[0]
    next_reg = pattern[1] if len(pattern) > 1 else None
    curr_str = string[0]

    def match(reg, char):
        return reg == char or reg == '.'

    if next_reg is None or next_reg != '*':
        return match(curr_reg, curr_str) and matchPattern(pattern[1:], string[1:])
    else:
        if next_reg == '*':
            return (match(curr_reg, curr_str) and matchPattern(pattern, string[1:])) or matchPattern(pattern[2:], string)
        else:
            return False
