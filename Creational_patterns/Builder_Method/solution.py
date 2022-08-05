# Abstract course
class Course:
 
    def __init__(self):
        self.Price()
        self.available_batches()
 
    def Price(self):
        raise NotImplementedError
 
    def available_batches(self):
        raise NotImplementedError
 
    def __repr__(self):
        return 'Price : {0.price} | Batches Available : {0.batches}'.format(self)

# concrete course
class Cooking(Course):
 
    """ Class for Cooking """
 
    def Price(self):
        self.price = 11000
    
    def available_batches(self):
        self.batches = 5
 
 
# concrete course
class Dancing(Course):
 
    """Class for Dancing"""
 
    def Price(self):
        self.price = 15000

    def available_batches(self):
        self.batches = 4

# concrete course 
class Coding(Course):
 
    """Class for Coding"""
 
    def Price(self):
        self.price = 35000

    def available_batches(self):
        self.batches = 9
 
# Complex Course
class ComplexCourse:
 
    def __repr__(self):
        return 'Price : {0.price} | available_batches: {0.batches}'.format(self)
 
# Complex course
class Complexcourse(ComplexCourse):
 
    def Price(self):
        self.price = 7000
 
    def available_batches(self):
        self.batches = 6
 
# construct course
def construct_course(cls):
 
    course = cls()
    course.Price()
    course.available_batches()
 
    return course    # return the course object

# main method
if __name__ == "__main__":
 
    code = Coding()    # object for Coding class
    cook = Cooking()    # object for Cooking class
    dance = Dancing()    # object for Dancing class
 
    complex_course = construct_course(Complexcourse)
    print(complex_course) #price : 7000 | available_batches: 6