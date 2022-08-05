# classic implementation of Singleton Design pattern
class Singleton:
 
    __shared_instance = 'ShikhaPandey'
 
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'ShikhaPandey':
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'ShikhaPandey':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
 
    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)

'''
O/P-

<__main__.Singleton object at 0x000001D89733DFD0>
<__main__.Singleton object at 0x000001D89733DFD0>
'''