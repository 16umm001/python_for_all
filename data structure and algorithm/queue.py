print("Queue -> FIFO -> First in First out")
class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.info = value
		self.link = None

class Queue(object):
	def __init__(self):
		self.start = None

	def viewQueue(self):
		if self.start == None:
			print("List is empty \n")
		else :
			print("List is: ")	
			p = self.start
			while p is not None:
				print(p.info," ",end = ' \n')
				p = p.link
			

	def push(self):
		data = int(input("Enter data to be pushed"))
		temp = Node(data)
		if self.start is None:
			self.start = temp
			return
		p = self.start
		while p.link is not None:
			p = p.link
		p.link = temp

	def pop(self):
		if self.start is None:
			return
		self.start = self.start.link			

list = Queue()
while True :
	print("-"*33)
	print("| Operation menu.               |")
	print("| 1. view Queue                 |")
	print("| 2. pust element to Queue.     |")
	print("| 3. pop element out from Queue |")
	print("| 4. Exit                       |")
	print("-"*33)

	option = int(input("choose your option"))
	if option == 1 :
		list.viewQueue()
	if option == 2:
		list.push()
	if option == 3:
		list.pop()
	if option == 4:
		exit()			


