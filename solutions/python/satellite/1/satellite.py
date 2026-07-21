def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError('traversals must have the same length')
    if set(preorder) != set(inorder):
        raise ValueError('traversals must have the same elements')
    if len(preorder) != len(set(preorder)):
        raise ValueError('traversals must contain unique items')
    return build_tree(preorder, inorder)
def build_tree(preorder, inorder):
    if len(preorder) == 0:
        return {}
    value = preorder[0]
    idx = inorder.index(value)
    return {
        'v': value,
        'l': build_tree(preorder[1:1+idx], inorder[:idx]),
        'r': build_tree(preorder[idx+1:], inorder[idx+1:]),
    }