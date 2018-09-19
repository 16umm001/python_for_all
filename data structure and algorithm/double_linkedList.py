class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList(object):
	"""docstring for DoubleLinkedList"""
	def __init__(self):
		self.head = None	


#diplay linked list

	def displayList(self):
		pass


# count nodes in linked list
	def countNode(self):
		pass

# serch element in the list
		
	def search(self,x):
		pass

#insert node at begining
	def insertBegining(self,data):
		pass

#insert node at end
	def insertEnd(self,data):
		pass

#create double linked list and store some data
	def createList(self):
		pass

#insert after given node
	def insertAfter(self,data,x):
		pass

#insert before given node
	def insertBefore(self,data,x):
		pass

#insert at given position
	def insert_at_position(self,data,x):
		pass

#delete any node
	def delete_node(self,x):
		pass			

#delete first node
	def delete_first_node(self):
		pass

#delete last node
	def delete_last_node(self):
		pass

#reverse list
	def reverse_list(self):
		pass

list = DoubleLinkedList()

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
	
