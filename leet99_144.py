# append order from bottom to top
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res , stack=[],[(root,False)]
        while stack:# inorder:  left -> root-> right
            node ,visited= stack.pop()
            if node: 
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right,False))
                    stack.append((node,True))                
                    stack.append((node.left,False))
        return res
    
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res , stack=[],[(root,False)]
        while stack:# postorder: root-> left -> right 
            node ,visited= stack.pop()
            if node: 
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right,False))                                    
                    stack.append((node.left,False))
                    stack.append((node,True))
        return res
    
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res , stack=[],[(root,False)]
        while stack:# postorder: left -> right -> root
            node ,visited= stack.pop()
            if node: 
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node,True))
                    stack.append((node.right,False))                                    
                    stack.append((node.left,False))
        return res