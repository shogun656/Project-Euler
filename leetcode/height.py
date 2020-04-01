class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Computes the diameter of binary
# tree with given root.
def max_depth(root, max_height):
    if not root:
        return 0

    left_height = max_depth(root.left, max_height)
    right_height = max_depth(root.right, max_height)

    return max(max_height, left_height, right_height) + 1


# Driver code
if __name__ == '__main__':
    root = NewNode(1)
    root.left = NewNode(2)
    root.right = NewNode(3)
    root.left.left = NewNode(4)
    root.left.right = NewNode(5)
    root.left.right.left = NewNode(5)
    root.left.right.left.right = NewNode(5)
    root.left.right.right = NewNode(5)
    root.left.right.right.right = NewNode(5)
    root.left.right.right.right.left = NewNode(5)
    root.left.right.right.right.left.right = NewNode(5)

    print("Max Depth is", max_depth(root, 0))
