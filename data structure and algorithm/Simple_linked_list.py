class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.info = value
		self.link = None

class LinkedList :
	def __init__(self):
		self.start = None

# display your linked list

	def displayList(self):
		if self.start == None:
			print("List is empty \n")
		else :
			print("List is: ")	
			p = self.start
			while p is not None:
				print(p.info," ",end = ' ')
				p = p.link

# count nodes in linked list
	def countNode(self):
		p = self.start
		n = 0
		while p is not None:
			n += 1
			p = p.link	
		print("no of nodes in list is=",n)	

# serch element in the list
		
	def search(self,x):
		position = 1
		p = self.start
		while p is not None:
			if p.info == x :
				print(x, "is at position  ", position)
				return True
			position +=1
			p=p.link
		else :
			print(x," not found in the list")	
			return False

	def insertBegining(self,data):
		temp = Node(data)
		temp.link = self.start
		self.start = temp	

	def insertEnd(self,data):
		temp = Node(data)
		if self.start is None:
			self.start = temp
			return
		p = self.start
		while p.link is not None:
			p = p.link
		p.link = temp
				
	def createList(self):
		n = int(input("Enter the number of nodes: "))
		if n == 0:
			return
		for i in range(n):
			data = int(input("Enter number to be inserted:"))
			self.insertEnd(data)			

	def insertAfter(self,data,x):
		p = self.start
		while p is not None:
			p.info == x
			break
		p = p.link
		if p is None:
			print(x," is not present in the list")	
		else :
			temp = Node(data)
			temp.link = p.link
			p.link = temp


	def insertBefore(self,data,x):
		if self.start is None:
			print("List is empty")
			return
		if x == self.start.info:
			temp = Node(data)
			temp.link = self.start
			self.start = temp
			return
		p = self.start
		while p.link is not None:
			if p.link.info == x:
				break
			p = p.link
		if p.link is None:
			print(x,"is not in list")
		else :
			temp = Node(data)
			temp.link = p.link
			p.link = temp

	def insert_at_position(self,data,x):
		if x == 1:
			temp = Node(data)
			temp.link = self.start
			self.start = temp
		p = self.start
		i = 1
		while i<x-1 and p is not None:
			p = p.link
			i += 1
		if p is None:
			print("you can not insert upto position ",i)
		else :
			temp = Node(data)
			temp.link = p.link
			p.link = temp 					

	def delete_node(self,x):
		if self.start is None:
			return
		if self.start.info == x:
			self.start = self.start.link
			return
		p = self.start
		while p.link is not None:
			if p.link.info == x:
				break
			p=p.link
		if p.link is None:
			print("element",x,"not in list")
		else :
			p.link = p.link.link			

	def delete_first_node(self):
		if self.start is None:
			return
		self.start = self.start.link	

	def delete_last_node(self):
		if self.start is None:
			return
		if self.start.link is None:
			self.start = None
			return
		p = self.start
		while p.link.link is not None:
			p = p.link
		p.link = None			

	def reverse_list(self):
		prev = None
		p = self.start
		while p is not None:
			next = p.link
			p.link = prev
			prev = p
			p = next
		self.start = prev
		self.displayList()
	

list = LinkedList()

while True:
	print("\n1.displayList")
	print("2.countNode")
	print("3.search")
	print("4.insertBegining")
	print("5.insertEnd")
	print("6.insertAfter")
	print("7.insertBefore")
	print("8.insert_at_position")
	print("9.delete_first_node")
	print("10.delete_last_node")
	print("11.delete any node")
	print("12.reverse_list")
	print("13. Create list")
	print("14.quit")

	option = int(input("Enter your choice"))
	if option == 13 :
		list.createList()

	elif option == 1 :
		list.displayList()

	elif option ==2 :
		list.countNode()

	elif option == 3:
		x = int(input("Enter number which you want to search in the list:")) 	
		list.search(x)

	elif option == 4:
		data = int(input("Enter number to be inserted:"))
		list.insertBegining(data)

	elif option == 5:
		data = int(input("Enter number to be inserted:"))
		list.insertEnd(data)

	elif option == 6:
		x =	int(input("Enter position after which you want to insert"))
		data = int(input("Enter data to be inserted"))
		list.insertAfter(data,x)

	elif option == 7:
		x =	int(input("Enter position before which you want to insert"))
		data = int(input("Enter data to be inserted"))
		list.insertBefore(data,x)		

	elif option == 8:
		x =	int(input("Enter position after which you want to insert"))
		data = int(input("Enter data to be inserted"))
		list.insert_at_position(data,x)

	elif option == 9 :
		list.delete_first_node()

	elif option == 10 :
		list.delete_last_node()		


	elif option == 11 :
		x = int(input("Enter value which has to be deleted"))
		list.delete_node(x)

	elif option ==12:
		list.reverse_list()


	elif option == 14 :
		exit()	
