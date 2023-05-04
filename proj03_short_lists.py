import list_node


def list_to_array(head):
    if head is None:
        return []
    else:
        values_array = []
        curr = head
        while curr is not None:
            values_array.append(curr.val)
            curr = curr.next
        return values_array


def array_to_list(data):
    head = None
    if len(data) == 0:
        return head
    elif len(data) == 1:
        head = list_node.ListNode(data[0])
        return head
    else:
        head = list_node.ListNode(data[0])
        cur = head
        for i in range(1, len(data)):
            node = list_node.ListNode(data[i])
            cur.next = node
            cur = node
        return head


def list_length(head):
    if head is None:
        return 0
    else:
        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next
        return count


def is_sorted(head):
    if head is None:
        print('head is none')
        return True
    if head is not None:
        length = list_length(head)
        if length == 1:
            return True
        else:
            cur = head
            while cur is not None:
                if cur.next is None:
                    return True
                else:
                    if cur.next.val < cur.val:
                        return False
                cur = cur.next
    return True


