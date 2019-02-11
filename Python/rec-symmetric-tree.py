class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def isMirror(node1, node2):
	if node1 == None and node2 == None:
		return True
	elif node1 == None or node2 == None:
		return False
	
	return node1.val == node2.val and \
			isMirror(node1.left, node2.right) and \
			isMirror(node2.right, node1.left)

def isSymmetric(root):
    return isMirror(root, root)

def main():
	root = TreeNode(1)

	child1 = TreeNode(2)
	child2 = TreeNode(2)
	root.left = child1
	root.right = child2

	child3 = TreeNode(3)
	child4 = TreeNode(4)
	child5 = TreeNode(4)
	child6 = TreeNode(3)
	child1.left = child3
	child1.right = child4
	child2.left = child5
	child2.right = child6

	print(isSymmetric(root)) # => True

	child2.right = None
	print(isSymmetric(root)) # => False

if __name__ == "__main__":
	main()

