class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(llist, k):
   cont = 0
   val = 0
   while cont < k:
       pass




# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))



# Order should now be 3, 4, 1, 2
#print(rotate_list(llist, 2))
# 3412
from operator import itemgetter

l = ["asd", "ase", "aaa", "bac", "bab"]
print(l)
l = sorted(l)
print(l)


l = [[1, "asd"], [2,"ase"], [3,"aaa"], [5,"bac"], [4,"bab"], [0, "aaa"]]

l = sorted(l, key=itemgetter(1,0))
print(l)