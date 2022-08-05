# Builder Method

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.

- **Problems we face without Builder Method:**
    - Consider wanting to enrol in one of the top batches of an institute. You will thus visit there and enquire about the course's fees, available times, and batches. They will explain the courses, their fee structures, the available times, and batches after you have a look at the system.
    Our primary goal when designing the system is to make it flexible, dependable, organised, and lubricative. Unskilled programmers will make a separate and unique class for each and every course offered by the institute. Then, even if it is not always necessary, they will build separate object instantiations for each and every class. The main problem will arise when institute will start new courses and developers have to add new classes as well because their code is not much flexible.

    - [Let's examine the code for the issue that can arise if we don't use the builder function.](problem.py)

- **Solution using Builder design pattern**
    - Any course from institute should be our ultimate output. It could be Cooking, Dancing, or Coding. Before selecting a certain course, we must take a number of measures, including researching the course information, syllabus, cost, scheduling, and batches. Here, we can choose from a variety of courses offered by the institute utilising the same procedure.That’s the benefit of using the builder Pattern.

- [Solution using Builder method](solution.py)

- **Merits of using Builder method**
    - *Reusability:* We may use the same construction code we used to create the different representations of the items to create other representations.
    - *Single Responsibility Principle:* We can separate out both the business logic as well as the complex construction code from each other.
    - *Construction of the object:* Here we construct our object step by step, defer construction steps or run steps recursively.

- **Demerits of using Builder method**
    - *Code complexity increases:* The complexity of our code increases, because the builder pattern requires creating multiple new classes.
    - *Mutability:* It requires the builder class to be mutable
    - *Initialization:* Data members of the class are not guaranteed to be initialized.

- **Applicability**
    - The Builder Method allows you to construct the products step-by-step. Even, we can defer the execution of some steps without breaking the final product. To create an object tree, it is handy to call the steps recursively.It prevents the client code from fetching the incomplete data because it doesn’t allow the exposing of an unfinished object.
    - The Builder pattern is applicable when construction of various representations of the product involves similar steps that differ only in the details. The base builder interface is used to define all the construction steps while these steps are implemented by concrete builders.
  
