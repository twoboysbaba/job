#输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class Node(object):
    def __init__(self):
        self.val = None
        self.next = None

class ListNode(object):
    def __init__(self):
        self.cur_node = None
    def add(self,data):
        node = Node()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node


def printListFromTailtoHead(listNode):
    if not listNode:
        return []
    p = listNode.cur_node
    stack= []
    res = []
    while p:
        stack.append(p.val)
        p = p.next
    print(stack)
    for i in range(len(stack)-1,-1,-1):
        res.append(stack[i])
    return res



listNode = ListNode()
listNode.add(1)
listNode.add(2)
listNode.add(3)

print(printListFromTailtoHead(listNode))
