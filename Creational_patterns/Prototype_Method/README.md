# Prototype Method
## Also known as: Clone

Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes. It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object. This method provides a way to copy the original object and then modify it according to our needs.

- **Problems we face without Prototype Method:**
    - Let’s understand the example of Courses At Institute that provides courses like Cooking, Dancing, Coding, etc. Now we want to create the exact copy of this object. How an ordinary developer will go? 
    He/She will create a new object of the same class and will apply all the functionalities of the original objects and copy their values. But we can not copy each and every field of the original object as some may be private and protected and are not available from the outside of the object itself. 
    Problems are not over here! you also become dependent on the code of other class which is certainly not a good practice in Software Development. Creating objects for similar courses, again and again, is not a good task to utilize the resources in a better way. 

    - [Let's examine the code for the issue that can arise if we don't use the Prototype function.](problem.py)

- **Solution using Prototype design pattern**
    - To deal with such problems, we use the Prototype method. We would create separate classes for Courses_At_inst and Course_At_inst_Cache which will help us in creating the exact copy of already existing object with the same field properties. This method delegates the cloning process to the actual objects that are being cloned. Here we declare a common interface or class which supports object cloning which allows us to clone the object without coupling our code to the class of that method. 
    An object that supports cloning is called as Prototype. 

- [Solution using Prototype method](solution.py)

- **Merits of using Prototype method**
    - *Less number of SubClasses :* All the other Creational Design Patterns provides a lot of new subClasses which are definitely not easy to handle when we are working on a large project. But using Prototype Design Pattern, we get rid of this.
    - *Provides varying values to new objects:*  All the highly dynamic systems allows you to define new behavior through object composition by specifying values for an object’s variables and not by defining new classes.
    - *Provides varying structure to new objects:* Generally all the applications build objects from parts and subparts. For convenience, such applications often allows you instantiate complex, user-defined structures to use a specific subcircuit again and again.

- **Demerits of using Prototype method**
    - *Abstraction:* It helps in achieving the abstraction by hiding the concrete implementation details of the class.
    - *Waste of resources at lower level:*  It might be proved as the overkill of resources for a project that uses very few objects

- **Applicability**
    -  Prototype method provides the way to implement the new objects without depending upon the concrete implementation of the class.
    - Prototype method is also used to solve the recurring and complex problems of the software development.
  
