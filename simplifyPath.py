# Given an absolute (Unix-style) path, simplify it.

# Example:
# path = "/home/" => "/home"
# path = "/a/./b/../../c/" => "/c"
# path = "/../" => "/"
# path = "/home//foo/" => "/foo"

def simplifyPath(path):
    result = []
    content = path.split('/')
    for word in content:
        if word:
            if word == '..':
                try:
                    result.pop()
                except:
                    result = []
            elif word != '.':
                result.append(word)
    return '/' + '/'.join(result)
