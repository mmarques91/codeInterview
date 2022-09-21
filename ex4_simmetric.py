def are_simmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif (root1 is None and root2 is None) or (root1.value != root2.value):
        return False
    else:
        are_simmetric(root1.left, root2.right)
        are_simmetric(root1.right, root2.left)

def is_simmetric(root):
    if root is None:
        return True
    are_simmetric(root.left, root.right)
