# Abstract Factory Method

Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes. The abstract factory pattern is also called factory of factories. It includes an interface, which is responsible for creating objects related to Factory. 
Using the abstract factory method, we have the easiest ways to produce a similar type of many objects. 
It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business, platform choice, etc.

- **Problem we face without Abstract Factory Method:**
    - Consider wanting to enrol in one of the top batches of a particular course. As a result, you will visit there and inquire about the courses that are offered, their fees, their schedules, and other crucial information. They will merely examine their system and provide you with all the details you required. looks easy? Consider how the developers created a system that is so well-organized and how their website is so user-friendly.

    Developers will make unique classes for each course which will contain its properties like Fee structure, timings, and other things. But how they will call them and how will they instantiate their objects?

    Here's where the issue occurs. Let's say there were just 3–4 courses offered initially, but later, 5 new courses were added.
    As a result, we must manually instantiate their objects, which is undesirable from the developer's perspective.

    - [Code for reference without using the abstract factory method](problem.py)

- **Solution using Abstract Factory design pattern**
    - Its solution is to replace the straightforward object construction calls with calls to the special abstract factory method. Actually, there will be no difference in the object creation but they are being called within the factory method. 
    Now we will create a unique class whose name is All_course which will handle all the object instantiation automatically. Now, we don’t have to worry about how many courses we are adding after some time.

    - [Solution using Abstract Factory method](solution.py)

- **Merits of using Abstract Factory method**
    - This pattern is particularly useful when the client doesn’t know exactly what type to create. 
        - It is simple to offer new product variations without compromising the current client code.
        - Products which we are getting from the factory are compatible with one another.

- **Demerits of using Abstract Factory method**
    - Our simple code may become complicated due to the existence of a lot of classes.
    - We end up with a huge number of small files i.e, cluttering of files.

- **Applicability**
    - Most commonly, abstract factory method pattern is found in the sheet metal stamping equipment used in the manufacture of automobiles.
    - It can be used in a system that has to process reports of different categories such as reports related to input, output, and intermediate transactions.
