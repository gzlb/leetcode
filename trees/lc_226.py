import Optional 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #Base Case
            return root
        invertTree(root.left) #Call the left substree
        invertTree(root.right)  #Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root # Return the root