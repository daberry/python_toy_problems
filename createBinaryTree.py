def create_binary_search_tree(array):
    midpoint = (len(array) - 1) / 2
    mid = array[midpoint]
    left = midpoint - 1
    right = midpoint + 1
    tree = BinarySearchTree(mid)
    while left > -1 and right < len(array) + 1:
        tree.insert(array[left])
        left -= 1
        tree.insert(array[right])
        right += 1
    return tree
