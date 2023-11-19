from collections import deque
from typing import Optional, List 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q:TreeNode) -> TreeNode: 
     
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    else:  
        return root 
