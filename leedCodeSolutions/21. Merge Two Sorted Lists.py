from ListNode import ListNode

def solu(list1,list2):

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = solu(list1.next,list2)
        # print(list1.val)
        return list1
    else:
        list2.next = solu(list1,list2.next)
        # print(list2.val)
        return list2


def printl(head):
    while head is not None:
        print(head.val)
        head = head.next
def createInp(list1):
    listHead = None
    listp = None
    for i in range(len(list1)):
        if i == 0 :
            listHead = ListNode(list1[i])
            listp = listHead
        else:
            listp.next = ListNode(list1[i])
            listp = listp.next

    return listHead


list1 = [1,2,5,1,2]
list2 = [1,3,4]
list1 = createInp(list1)
list2 = createInp(list2)

printl(solu(list1,list2))