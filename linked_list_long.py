
def is_sorted(head):
    cur =head
    if head is None:
        return True
    while cur.next is not None:
        if cur.next.val >= cur.val:
            cur= cur.next
        else:
            return False
    return True

def list_sum(head):
    cur=head
    if head is None:
        return 0
    count=0
    while cur is not None:
        count+=cur.val
        cur=cur.next
    return count

def partition_list(head):
    cur= head
    if head is None:
        return True
    while cur.next is not None:
        ''
