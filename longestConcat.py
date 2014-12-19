# Given a sorted list of words, find the longest compound word in the list
# that is constructed by concatenating the words in the list. 

# We'll be using a prefix tree, or trie, to solve this
# First, define our trie node

class Node:
    def __init__(self, letter=None, isTerminal=False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal

# Now define our trie class

class Trie:
    def __init__(self):
        self.root = Node('')

    def __repr__(self):
        self.output([self.root])
        return ''

    def output(self, currentPath, indent=''):
        #Depth-first search
        currentNode = currentPath[-1]
        if currentNode.isTerminal:
            word = ''.join([node.letter for node in currentPath])
            print index + word
            indent += '    '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:] + [node], indent)

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True

    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isTerminal

    def getAllPrefixesOfWord(self, word):
        prefix = ''
        prefixes = []
        current = self.root
        for letter in word:
            if letter not in current.children:
                return prefixes
            current = current.children[letter]
            prefix += letter
            if current.isTerminal:
                prefixes.append(prefix)
        return prefixes

# Now for our actual function

def longestConcat(words):
    # Add words to the trie, and pairs to the queue
    trie = Trie()
    queue = collections.deque()
    for word in words:
        prefixes = trie.getAllPrefixesOfWord(word)
        for prefix in prefixes:
            queue.append( (word, word[len(prefix):]) )
        trie.insert(word)

    # Process the queue
    longestConcat = ''
    maxLength = 0
    while queue:
        word, suffix = queue.popleft()
        if suffix in trie and len(word)&gt;maxLength:
            longestConcat = word
            maxLength = len(word)
        else:
            prefixes = trie.getAllPrefixesOfWord(suffix)
            for prefix in prefixes:
                queue.append( (word, suffix[len(prefix):]) )
    return longestConcat
