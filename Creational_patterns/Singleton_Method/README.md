# Singleton Method

Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.
It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.

- **Method 1: Monostate/Borg Singleton Design pattern**
    - Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class, there are multiple instances that share the same state. Here we don’t focus on the sharing of the instance identity instead we focus on the sharing state. 
    - [Code](Borg.py)

- **Creating a singleton in Python**
    - In the classic implementation of the Singleton Design pattern, we simply use the static method for creating the getInstance method which has the ability to return the shared resource. We also make use of the so-called Virtual private Constructor to raise the exception against it although it is not much required.
    - [Code](singleton.py)

- **Merits of using the Singleton Method:** 
    - Initializations: An object created by the Singleton method is initialized only when it is requested for the first time.
    - Access to the object: We got global access to the instance of the object.
    - Count of instances: In singleton, method classes can’t have more than one instance

- **Demerits of using the Singleton Method:**
    - *Multithread Environment:* It’s not easy to use the singleton method in a multithread environment, because we have to take care that the multithread wouldn’t create a singleton object several times.
    - *Single responsibility principle:* As the Singleton method is solving two problems at a single time, it doesn’t follow the single responsibility principle.
    - *Unit testing process:* As they introduce the global state to the application, it makes the unit testing very hard.

- **Applicability**
    - Controlling over global variables: In the projects where we specifically need strong control over the global variables, it is highly recommended to use Singleton Method
    - Daily Developers use: Singleton patterns are generally used in providing the logging, caching, thread pools, and configuration settings and are often used in conjunction with Factory design patterns.