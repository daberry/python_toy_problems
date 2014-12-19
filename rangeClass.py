class Range(object):
    def __init__(self, start, end, step):
        if end == None:
            end = start
        if step == None and start < end:
            step = 1
        if step == None and not (start < end):
            step = -1

    def size(self)

