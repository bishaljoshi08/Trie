
class TrieNode():
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.end = False

class Trie():
    def __init__(self):
        self.root = TrieNode('*')

    def isAvailable(self,word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.end

    def addWord(self,word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        current_node.end = True      

    def deleteWord(self,word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                print('You are trying to selete a non existing word.')
                return
            previous_node = current_node
            current_node = current_node.children[letter]
        print(current_node.children)
        if current_node.children:
            if self.isAvailable(word):
                return
            else:
                current_node.end = False
        else:
            previous_node.children.pop(current_node.value)
            self.deleteWord(word[:-1])
        




trie = Trie()
trie.addWord('hari')
trie.addWord('har')
trie.addWord('harr')
trie.addWord('harry')
trie.addWord('harris')
# trie.addWord('rajan')
# trie.addWord('rajani')
# trie.addWord('raj')
trie.deleteWord('hariom')
trie.deleteWord('harry')
# trie.deleteWord('rajan')
print(trie.isAvailable('har'))
print(trie.isAvailable('harry'))
print(trie.isAvailable('hari'))
print(trie.isAvailable('sita'))


                
