class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

def find(root, target):
    if not root:
        return str(target) + ' not found'

    if target == root.value:
        return str(root.value) + ' found'
    elif target < root.value:
        return find(root.left, target)
    else:
        return find(root.right, target)
        
def main():
    head = Node(2)
    a = Node(1)
    b = Node(3)

    head.left = a
    head.right = b

    print(find(head, 2))
    print(find(head, 1))
    print(find(head, 3))
    print(find(head, 5))

if __name__ == "__main__":
    main()