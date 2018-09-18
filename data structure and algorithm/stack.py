print("Stack -> LIFO -> Last in First out")
class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.info = value
		self.link = None

class Stack(object):
	def __init__(self):
		self.start = None

	def viewStack(self):
		if self.start == None:
			print("List is empty \n")
		else :
			print("List is: ")	
			p = self.start
			while p is not None:
				print(p.info," ",end = ' \n')
				p = p.link
			

	def push(self):
		data = int(input("Enter data to be inserted"))
		temp = Node(data)
		temp.link = self.start
		self.start = temp		
			
	def pop(self):
		if self.start is None:
			return
		self.start = self.start.link		

list = Stack()
while True :
	print("-"*33)
	print("| Operation menu.               |")
	print("| 1. view stack                 |")
	print("| 2. pust element to stack.     |")
	print("| 3. pop element out from stack |")
	print("| 4. Exit                       |")
	print("-"*33)

	option = int(input("choose your option"))
	if option == 1 :
		list.viewStack()
	if option == 2:
		list.push()
	if option == 3:
		list.pop()
	if option == 4:
		exit()			


