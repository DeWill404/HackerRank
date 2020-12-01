class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
        
    def calculateHeight(self, node, height):
        h = height
        if node:
            h = max(h, self.calculateHeight(node.left, height+1))
            h = max(h, self.calculateHeight(node.right, height+1))
        return h

    def getHeight(self,root):
        return self.calculateHeight(root, 0)-1
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
