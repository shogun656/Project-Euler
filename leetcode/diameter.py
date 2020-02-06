# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1


class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to find height of a tree
def height(root, ans):
    if not root:
        return 0

    left_height = height(root.left, ans)
    right_height = height(root.right, ans)

    # update the answer, because diameter
    # of a tree is nothing but maximum
    # value of (left_height + right_height + 1)
    # for each node
    height_num = 1 + left_height + right_height
    if height_num > ans[0]:
        ans[0] = height_num

    return 1 + max(left_height, right_height)


# Computes the diameter of binary
# tree with given root.
def diameter(root):
    if not root:
        return 0
    ans = [1]  # This will store

    # the final answer
    height(root, ans)
    return ans[0]


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

    print("Diameter is", diameter(root))
