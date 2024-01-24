# -*- coding: utf-8 -*-
"""DS(17/1/24).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MFqD9CAooyFuzWqrpKSyHFSPadTL3HxV
"""

class Node:
  def __init__(self,x):
    self.data=x
    self.next=None
class Stack:
  def __init__(self):
    self.top=None
  def push(self):
    x=int(input("Enter element "))
    new=Node(x)
    if self.top is None:
      self.top=new
      self.top.next=None
    else:
      new.next=self.top
      self.top=new
  def pop(self):
    if self.top is None:
      print("Stack is empty ")
    elif self.top.next is None:
      print("Popped element ", self.top.data)
      self.top=None
    else:
      temp=self.top
      print("Popped element ",self.top.data)
      self.top=temp.next
      temp=None
  def display(self):
    if self.top is None:
      print("Stack is empty")
    else:
      print("Elements are ")
      temp=self.top
      while temp:
        print(temp.data)
        temp=temp.next
      print("TOP OF STACK ",self.top.data)
  def overflow():
    if len(Stack)==3:
      print("Stack overflow ")
    else:
      print("")

s=Stack()
while True:
  opt=int(input("1.Push 2.Pop 3.Display 4.Quit "))
  if opt==1:
    s.push()
  elif opt==2:
    s.pop()
  elif opt==3:
    s.display()
  else:
    break

"""

# steps required to convert infix to postix Expression:
# a. if character is left paranthesis, pushed to the stack
# b. if character is an operand add to the postfix expression
# c. if character is an operator check whether stack is empty
#  1. if stack is empty push operator into stack
#  2. if stack is not empty check priority of operator
#          1. if priority is greater than operator present at top of the stack then push operator into stack
#          2. if priority of operator is lesser than or equal to operator present on top of stack then pop the operator from stack and add to postfix expression and go to 1
#d.
#e. after reading all characters if stack is not empty then pop and add to postfix expression"""