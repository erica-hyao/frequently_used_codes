class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def InOrderTraversal(self,root):
        if not root:
            return []
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        InOrder = []

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                InOrder.append(stack[-1].val)
        return InOrder

    def PreOrderTraversal(self,root):
        PreOrder = []
        if not root:
            return PreOrder
        left = self.PreOrderTraversal(root.left)
        right = self.PreOrderTraversal(root.right)
        PreOrder.append(root.val)
        PreOrder.append(left)
        PreOrder.append(right)
        return PreOrder
