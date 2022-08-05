# Singleton Borg pattern
class Borg:

	# state shared by each instance
	__shared_state = dict()

	# constructor method
	def __init__(self):

		self.__dict__ = self.__shared_state
		self.state = 'StateofInstitute'

	def __str__(self):

		return self.state


# main method
if __name__ == "__main__":

	person1 = Borg() # object of class Borg
	person2 = Borg() # object of class Borg
	person3 = Borg() # object of class Borg

	person1.state = 'Coding' # person1 changed the state
	person2.state = 'Dancing'	 # person2 changed the state

	print(person1) # output --> Dancing
	print(person2) # output --> Dancing

	person3.state = 'Cooking' # person3 changed the
	# the shared state

	print(person1) # output --> Cooking
	print(person2) # output --> Cooking
	print(person3) # output --> Cooking

'''
O/P-

Dancing
Dancing
Cooking
Cooking
Cooking
'''
