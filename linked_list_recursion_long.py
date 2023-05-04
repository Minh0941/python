
'''Author: Minh Le
    Name: linked_list_recursion_long.py
    Purpose:  Various functions Russ wants me to do...
    I hope you're having a great day Kapua
'''
def annoying_fibonacci_sequence(n):
    '''Prints out a fibonacci sequence reciursively based on 
    several hard inputs and user input
    Param: n= user input of number of fibonacci sequence to print

    '''
    if n ==0:
        return []
    if n==1:
        return[0]
    if n==2:
        return[0,1]
    if n==3:
        return[0,1,1]
    if n==4:
        return annoying_fibonacci_sequence(n-1)+ [2]
    if n==5:
        return annoying_fibonacci_sequence(n-1)+ [3]
    if n==6:
        return annoying_fibonacci_sequence(n-1)+[5]
    if n>6:
        temp= annoying_fibonacci_sequence(n-1)
        return temp +[temp[-1]+temp[-2]]


from list_node import*  
def array_to_list_recursive(data):
    ''' 
    Turns a list into a linked list recursively by turning 
    each new array val into a new head of the linked list. 
    Param: Data =  Array structure that the user can input into this function
    Return: head= linked list that you created
    '''
    if len(data) ==0:
        return None
    head = ListNode(data[0])
    if len(data) >1:
        head.next= array_to_list_recursive(data[1:])
    return head

def accordion_recursive(head):
    '''
    Doesn't create or delete linked list nodes but merely rearranges them 
    recurrsively so that every other linked list node is ommitted
    Param: Head= linked list that user inputs
    Return head= same linked list but ommited
    '''
    if head is None or head.next is None:
        return None
    cur= head.next
    head = cur
    if head is not None:
        head.next = accordion_recursive(head.next)
    return head

def pair_recursive(head1,head2):
    '''
    Turns two linked lists into one containing tuples as vals 
    Param: Head1: Linked list 1
           Head2: Linked List 2
    Return: head= new linked list with tuples
    '''
    if head1 is None or head2 is None:
        return None
    head= (head1.val,head2.val)
    head = ListNode(head)
    if head1.next and head2.next is not None:
        head.next = pair_recursive(head1.next,head2.next)
    return head