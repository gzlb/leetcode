from collections import deque
from typing import Optional, List 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def level_order(root: TreeNode) -> List[List[int]]:
     
    res = []

    q = deque()
    q.append(root)

    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level.append(node.val)

                q.append(node.left)
                q.append(node.right)
            
        if level: 
            res.append(level)

    return res 

