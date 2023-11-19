from collections import deque
from typing import Optional, List 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def kthSmallest_dfs_early_stopping(root, k):
	res = []
	def _inorder(node):
		if not node: return
		_inorder(node.left)
		if len(res) == k:
			return
		res.append(node.val)
		_inorder(node.right)
	_inorder(root)
	return res[-1]