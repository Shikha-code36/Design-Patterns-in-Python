import random
 
class All_Courses:
 
    """ Portal for courses """
 
    def __init__(self, courses_factory = None):
        """course factory is out abstract factory"""
 
        self.course_factory = courses_factory
 
    def show_course(self):
 
        """creates and shows courses using the abstract factory"""
 
        course = self.course_factory()
 
        print(f'We have a course named {course}')
        print(f'its price is {course.price()}')

class Cooking:
 
    """ Class for Cooking """
 
    def price(self):
        return 11000
 
    def __str__(self):
        return "Cooking"
 
class Dancing:
 
    """Class for Dancing"""
 
    def price(self):
        return 15000
 
    def __str__(self):
        return "Dancing"
 
class Coding:
 
    """Class for Coding"""
 
    def price(self):
        return 35000
 
    def __str__(self):
        return "Coding"
 
def random_course():
 
    """A random class for choosing the course"""
 
    return random.choice([Coding, Dancing, Cooking])()
 
 
if __name__ == "__main__":
 
    course = All_Courses(random_course)
 
    for i in range(5):
        course.show_course()

'''
O/P-

We have a course named Coding
its price is 35000
We have a course named Cooking
its price is 11000
We have a course named Coding
its price is 35000
We have a course named Coding
its price is 35000
We have a course named Cooking
its price is 11000
'''