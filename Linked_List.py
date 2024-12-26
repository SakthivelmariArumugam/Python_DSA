class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
  
  def front_append(self,value):
    NewNode=Node(value)
    if self.head==None:
      self.head=NewNode
      self.tail=NewNode
    else:
      NewNode.next=self.head
      self.head=NewNode
  def end_append(self,value):
    NewNode=Node(value)
    if self.head==None:
      self.head=NewNode
      self.tail=NewNode
    else:
      self.tail.next=NewNode
      self.tail=NewNode
  def Iterating(self):
    Iterator=self.head
    if self.head==None:
      print("list is empty")
      return
    while Iterator:
      print(Iterator.value)
      Iterator=Iterator.next
  def position(self,pos):
    first=self.head
    count=1
    while first:
      if(count==pos):
        return first
      count=count+1
      first=first.next
  def Insert_Middle(self,pos,value):
    NewNode=Node(value)
    pos=self.position(pos)
    NewNode.next=pos.next
    pos.next=NewNode
  def remove_front(self):
    if self.head==None:
      return
    self.head=self.head.next
  def remove_last(self):
    if self.head is None:  
        return
    if self.head == self.tail:  
        self.head = None
        self.tail = None
        return
    iterator = self.head
    while iterator.next != self.tail:  
        iterator = iterator.next
    iterator.next = None 
    self.tail = iterator 
  def remove_position(self,pos):
     pos=self.position(pos)
     if self.head==self.tail:
       return None
     pos.next=pos.next.next

    
l1=LinkedList()
l1.front_append(10)
l1.end_append(20)
l1.front_append(50)
l1.front_append(60)
l1.end_append(100)
l1.Insert_Middle(3,500)
l1.Insert_Middle(4,600)
l1.remove_front()
l1.remove_front()
l1.remove_front()
l1.remove_last()
l1.remove_position(2)
l1.remove_position(1)
l1.Iterating()