class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def InOrderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        PreOrder = []
        if not root:
            return PreOrder
        left = self.PreOrderTraversal(root.left)
        right = self.PreOrderTraversal(root.right)
        PreOrder.append(root.val)
        PreOrder.append(left)
        PreOrder.append(right)
        return PreOrder
    
    def LevelOrderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        LevelOrder = []
        while queue:
            level = []
            # return: [[1],[2,3]], so we need to use the for loop
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            LevelOrder.append(level)
        return LevelOrder
