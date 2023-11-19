import Optional 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 

    if p is None or q is None:
            return p == q
    
    return (p.val== q.val) and same_tree(p.left, q.left) and same_tree(p.right, q.right)