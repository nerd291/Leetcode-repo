# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3 = []
        for x in range (len(l1)+len(l2)):
            if (x<=len(l1)):
                l3[x].append(l1[x])
            elif(x>len(l1)):
                l3.append(l2[x-len(l1)])

                
obj = Solution()
obj.mergeTwoLists(obj,[1,2,3],[4,5,6])
        