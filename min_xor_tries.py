class TrieNode:
    def __init__(self):
        self.child={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,nums):
        node=self.root
        for i in range(31,-1,-1):
            bit = (nums>>i)&1
            if bit not in node.child:
                node.child[bit]=TrieNode()
            node=node.child[bit]
        node.end=True
    def max_xor(self,num):
        node=self.root
        xor=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if bit in node.child:
                node=node.child[bit]
            else:
                xor|=1<<i
                node=node.child[1-bit]
        return xor
def max_xor(arr):
    t=Trie()
    t.insert(arr[0])
    max_xor_val=0
    for num in arr[1:]:
        curr_val=t.max_xor(num)
        max_xor_val=max(max_xor_val,curr_val)
        t.insert(num)
    return max_xor_val
arr=list(map(int,input().split()))
print(max_xor(arr))