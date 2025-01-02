class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
    self.tail=None
  def Add_Node_Front(self,data):
    NewNode=Node(data)
    if self.head==None:
      self.head=NewNode
      self.tail=NewNode
    else:
      NewNode.next=self.head
      self.head=NewNode
  def Node_dipplay(self):
    current=self.head
    while current:
      print(current.data,end=" ")
      current=current.next
    print("\n")
  def Reverse_Linkedlist(self):
    prev=None
    current=self.head
    while current:
      next=current.next
      current.next=prev
      prev=current
      current=next
    self.head=prev

l1=Linkedlist()
l1.Add_Node_Front(10)
l1.Add_Node_Front(20)
l1.Add_Node_Front(30)
l1.Add_Node_Front(40)
l1.Add_Node_Front(50)
l1.Node_dipplay()
l1.Reverse_Linkedlist()
l1.Node_dipplay()