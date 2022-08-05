# Abstract course
class Course:
 
    def __init__(self):
        self.Fee()
        self.available_batches()
 
    def Fee(self):
        raise NotImplementedError
 
    def available_batches(self):
        raise NotImplementedError
 
    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# concrete course
class Cooking:
 
    """ Class for Cooking """
 
    def price(self):
        return 11000
    
    def available_batches(self):
        self.batches = 5
 
    def __str__(self):
        return "Cooking"
 
# concrete course
class Dancing:
 
    """Class for Dancing"""
 
    def price(self):
        return 15000

    def available_batches(self):
        self.batches = 4
 
    def __str__(self):
        return "Dancing"

# concrete course 
class Coding:
 
    """Class for Coding"""
 
    def price(self):
        return 35000

    def available_batches(self):
        self.batches = 9
 
    def __str__(self):
        return "Coding"
 
# Complex Course
class ComplexCourse:
 
    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)
 
# Complex course
class Complexcourse(ComplexCourse):
 
    def Fee(self):
        self.fee = 7000
 
    def available_batches(self):
        self.batches = 6
 
# construct course
def construct_course(cls):
 
    course = cls()
    course.Fee()
    course.available_batches()
 
    return course    # return the course object

# main method
if __name__ == "__main__":
 
    code = Coding()    # object for Coding class
    cook = Cooking()    # object for Cooking class
    dance = Dancing()    # object for Dancing class
 
    complex_course = construct_course(Complexcourse)
    print(complex_course) #Fee : 7000 | available_batches: 6