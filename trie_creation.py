class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch]=TrieNode()
            node=node.child[ch]
        node.end=True
    def search(self,word):
        node=self._search_prefix(word)
        # since it searches for complete, the end of node must be true
        return node is not None and node.end==True
    def _search_prefix(self,word):
        node=self.root
        for ch in word:
            if ch not in word:
                return None
            #going to next node
            node=node.child[ch]
        return node
    def startwith(self,word):
        return self._search_prefix(word) is not None 
#object creation
trie=Trie()
#insert elements
trie.insert('apple')
trie.insert('mango')
trie.insert('orange')
print('insertion completed')
print(trie.search('apple'))
print(trie.search('man')) #false bcz there is no 'man' word separately
print(trie.startwith('app')) #startswith functions checks for matching prefixes so in this case returns True