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
 
# main method
if __name__ == "__main__":
 
    code = Coding()    # object for Coding class
    cook = Cooking()    # object for Cooking class
    dance = Dancing()    # object for Dancing class
 
    print(f'Name of the course is {code} and its price is {code.price()}')
    print(f'Name of the course is {cook} and its price is {cook.price()}')
    print(f'Name of the course is {dance} and its price is {dance.price()}')

'''
O/p

Name of the course is Coding and its price is 35000
Name of the course is Cooking and its price is 11000
Name of the course is Dancing and its price is 15000
'''