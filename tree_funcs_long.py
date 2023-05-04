
'''
Author: Minh Le
File Name: tree_funcs_long
Purpose: To run and create various types of trees. These include running through 
BST, normal trees, as well as sorting trees in_order, post_order
'''

from tree_node import *
def bst_search_loop(root,val):
    '''
    Definition: It searches through a BST without recursion for a val that the user inputs

    root: The BST the user can input
    val: The value the user is trying to find within the BST

    return:
    root: the root at which the value is at
    '''
    if root is None:
        return None
    while root is not None:
        if val > root.val:
            root= root.right
        elif val < root.val:
            root= root.left
        elif val == root.val:
            return root
    else:
        return None

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

def bst_insert_loop(root,val):
    '''
    Purpose: Insert a child into the BST at the correct
    
    root: the BST to search through and add a child
    val: A value to insert into BST

    return:
    root: New BST

    '''
    cur =root
    node = None
    if root is None:
        return TreeNode(val)
    while cur:
        node = cur
        if  val > cur.val:
            cur = cur.right
        elif val < cur.val:
            cur= cur.left
    if val < node.val:
        node.left= TreeNode(val)
    elif val > node.val:
        node.right=TreeNode(val)
    return root

def pre_order_traversal_print(root):
    '''
    Purpose to print out the Tree in pre order traversal order
    using only recursion

    root: The Tree that the user input
    '''
    if root is not None:
        print(root.val)
        pre_order_traversal_print(root.left)
        pre_order_traversal_print(root.right)
def in_order_traversal_print(root):
    '''
    Purpose to print out the Tree in in order traversal order
    using only recursion

    root: The Tree that the user input 
    '''
    if root is not None:
        in_order_traversal_print(root.left)
        print(root.val)
        in_order_traversal_print(root.right)
    
def post_order_traversal_print(root):
    '''
    Purpose to print out the Tree in post order traversal order
    using only recursion

    root: The Tree that the user input
    '''
    if root is not None:
        post_order_traversal_print(root.left)
        post_order_traversal_print(root.right)
        print (root.val)
def in_order_vals(root):
    '''
    Purpose to print out the Tree in in order traversal order
    using only recursion and its vals

    root: The Tree that the user input
    '''
    if root is None:
        return []
    return in_order_vals(root.left) + [root.val] +in_order_vals(root.right)
def bst_max(root):
    '''
    Purpose: to return the max value in the BST

    root: the BST tree the user inputs 
    '''
    if root is None:
        return 0
    while root.right is not None:
        root= root.right
    return root.val

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
    


