
class Cooking:
 
    """ Class for Cooking """
 
    def type(self):
        return "Indian and Italian"
 
    def __str__(self):
        return "Cooking"
 
class Dancing:
 
    """Class for Dancing"""
 
    def type(self):
        return "Hip Hop and Bhangra"
 
    def __str__(self):
        return "Dancing"
 
class Coding:
 
    """Class for Coding"""
 
    def type(self):
        return "Python and C++"
 
    def __str__(self):
        return "Coding"
 
# main method
if __name__ == "__main__":
 
    code = Coding()    # object for Coding class
    cook = Cooking()    # object for Cooking class
    dance = Dancing()    # object for Dancing class
 
    print(f'Name of the course is {code} and its type is {code.type()}')
    print(f'Name of the course is {cook} and its type is {cook.type()}')
    print(f'Name of the course is {dance} and its type is {dance.type()}')

'''
O/p

Name of the course is Coding and its type is Python and C++
Name of the course is Cooking and its type is Indian and Italian
Name of the course is Dancing and its type is Hip Hop and Break
'''