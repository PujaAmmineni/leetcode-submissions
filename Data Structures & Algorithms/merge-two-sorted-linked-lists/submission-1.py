class Solution:
    def mergeTwoLists(self, list1, list2):
        head = None
        tail = None

        while list1 and list2:
            if list1.val <= list2.val:
                picked = list1
                list1 = list1.next
            else:
                picked = list2
                list2 = list2.next

            if head is None:
                head = picked
                tail = picked
            else:
                tail.next = picked
                tail = picked

        # 🔑 IMPORTANT FIX
        if tail is None:
            return list1 or list2

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return head
