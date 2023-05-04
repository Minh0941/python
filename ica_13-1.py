from pkg_resources import empty_provider
import ListNode

class ArraySTack:
    def __init__(self):
        self._items= []
    def push(self,item):
        self._items.append(item)
    def  is_empty(self):
        if len(self._items)== 0:
            return True
        else:
            return False 
    def pop(self):
        return self._items.pop()


class ListStack:
    def __init__(self):
        self.head = None
    def push(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            new_node= ListNode(data)
            new_node.next= self.head
            self.head=new_node
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def pop(self):
        if self.head is None:
            return None
        else:
            popped= self.head.val
            self.head= self.head.next
            return popped
