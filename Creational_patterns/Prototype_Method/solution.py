# import the required modules

from abc import ABCMeta, abstractmethod
import copy


# class - Courses at Institute
class Courses_At_inst(metaclass = ABCMeta):
	
	# constructor
	def __init__(self):
		self.id = None
		self.type = None

	@abstractmethod
	def course(self):
		pass

	def get_type(self):
		return self.type

	def get_id(self):
		return self.id

	def set_id(self, sid):
		self.id = sid

	def clone(self):
		return copy.copy(self)

# class - Cooking course
class Cooking(Courses_At_inst):
	def __init__(self):
		super().__init__()
		self.type = "Indian and Italian"

	def course(self):
		print("Inside Cooking::course() method")

# class - Dancing Course
class Dancing(Courses_At_inst):
	def __init__(self):
		super().__init__()
		self.type = "Break and Bhangra"

	def course(self):
		print("Inside Dancing::course() method.")

# class - Coding Course
class Coding(Courses_At_inst):
	def __init__(self):
		super().__init__()
		self.type = "Python and C++"

	def course(self):
		print("Inside Coding::course() method.")

# class - Courses At GeeksforGeeks Cache
class Courses_At_inst_Cache:
	
	# cache to store useful information
	cache = {}

	@staticmethod
	def get_course(sid):
		COURSE = Courses_At_inst_Cache.cache.get(sid, None)
		return COURSE.clone()

	@staticmethod
	def load():
		Dance = Dancing()
		Dance.set_id("1")
		Courses_At_inst_Cache.cache[Dance.get_id()] = Dance

		Cook = Cooking()
		Cook.set_id("2")
		Courses_At_inst_Cache.cache[Cook.get_id()] = Cook

		Code = Coding()
		Code.set_id("3")
		Courses_At_inst_Cache.cache[Code.get_id()] = Code

# main function
if __name__ == '__main__':
	Courses_At_inst_Cache.load()

	Dance = Courses_At_inst_Cache.get_course("1")
	print(Dance.get_type())

	Cook = Courses_At_inst_Cache.get_course("2")
	print(Cook.get_type())

	Code = Courses_At_inst_Cache.get_course("3")
	print(Code.get_type())

'''
O/P-

Break and Bhangra
Indian and Italian
Python and C++
'''