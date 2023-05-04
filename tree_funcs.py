
def tree_count(root):
    count =0
    if root is None:
        return 0
    if root is not None:
        count+=1
    count= count+ tree_count(root.left)+tree_count(root.right) 
    return count

def tree_sum(tree):
    if tree is None:
        return 0
    sum = tree.val + tree_sum(tree.left) + tree_sum(tree.right)
    return sum

def tree_print(root):
    if root is None:
        return None
    if root is not None:
        print(root.val)
        tree_print(root.left)
        tree_print(root.right)

def tree_search(root, val):
    '''
    Purpose: Trying to find a value within a regular tree.

    root: The tree in which the user inputs
    val: the value that the user is trying to find 

    return:
    root:the root at which the val is at
    '''
    if root is None:
        return root
    if root.val ==val:
        return root
    if root is not None:
        right = tree_search(root.right,val)
        left= tree_search(root.left,val)
        if right:
            return right
        if left:
            return left



def tree_max(root):
    if root is None:
        return 0
    st=root.val
    right = tree_max(root.right)
    left = tree_max(root.left)
    if (left > st): 
        st = left  
    if (right > st):  
        st = right 
    return st 
