# Factory Method
## Also known as: Virtual Constructor

- Factory Method is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide which class or object to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.

- **Problems we face without Factory Method:**
    - Let's say we developed an app whose major function is to translate across languages; at the moment, our app only supports 10 different languages. Now that our app is very well-liked by users, there is an urgent need for it to support five more languages.
    It's wonderful news, indeed! not for the developers, just for the owner. Because the majority of the code is currently only connected with the currently supported languages, developers must alter the entire codebase, which is a very challenging operation to complete.

    - [Let's examine the code for the issue that can arise if we don't use the factory function.](problem.py)

- **Solution using Factory design pattern**
    - In the solution, we use the special factory method to call the construction object instead of using straight forward object construction. Both method of creating objects are quite similar but they are called within the factory method.

    - [Solution using Factory method](solution.py)

- **Merits of using Factory Method**

    - Factory methods are very useful in adding new types of product without distributing the existing client code.
    - It avoids the tight coupling between the products and the creator classes and objects.

- **Demerits of using Factory Method**

    - It will create the large number of small files or cluttering of the files.
    - The client might have the sub class to create a particular actual product object.

- **Applicability**
    - Its concept is same as the **polymorphism**, where we don't need to make changes in the client code. For example - Suppose we want to draw different shapes such as Rectangle, Square, Circle, etc. We can use the factory method to create the instance depending upon the user's input.
    In a cab application, we can book a 1- wheeler, 2- wheeler, 3-wheeler, and 4-wheeler. Here the user can book any of the rides which he wants to book. With the help of factory method, we can create a class named Booking which will help us to create the instance that takes the user's input. So here the developer doesn't need to change the entire code to add the new facility.
    Factory method removes the complex logical code that is hard to preserve. It also prevents us to change in codebase because modifying existing code can introduce the subtle bugs and change in the behavior.

- **Where to use factory Methods**

    - Replacing complex logical code
        - The majority of the time, logic like if/else/elif is used in the code, which makes it challenging to maintain when new paths are added and requirements change.
        The body of each logical path can be added using the factory method to the many declared functions or classes that have a common interface. The developer is able to provide the modification a concrete implantation.
    
    - Combining similar features under a common interface
        - Let's say we want to add the particular filter to an image. According to the user's input, the factory method will identify the precise filter. The actual implementation can be used in the factory method.

    - Supporting multiple implementations of the same features
        - The satellite photos must be converted from one coordinate system to another for a group of scientists. However, a system contains a number of algorithms to carry out the various levels of transformation. The user may be able to choose the best algorithm through the application. Based on this choice, factory methods can implement algorithms robustly.
    
    - Integrating related external series
        - Multiple external services are sought to be integrated by a video streaming application. Users of the application can find out where their video is coming from. According to a user preference, the Factory method produces the appropriate integration.

