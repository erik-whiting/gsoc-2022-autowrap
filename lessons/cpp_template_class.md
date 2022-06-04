[Home](../README.md)

## C++ Template Class Basics

I learned some interesting things about template classes in C++. Basically they are a means of creating classes that can be made of different data types. For examples I made `Array<T>` which could be an integer array or float array.

### Some interesting things I learned about template classes:

I would not have realized that member functions need their own template declaration outside of the template class. I learned that the convention in C++ for **non** template classes is to put the class definition in a header file and member functions in a `.cpp` file, but this doesn't work for tempalte classes.

The easiest solution is to just keep mmeber functions in the same file as the class definition (the `.h` file) but if that gets too long, you could also make a `.inl` file (for "inline") and include it at the bottom of the `.h` file inside the header guard.

There is a third option which I think is best and that is to use three different files: the header, the member functions, and a `templates.cpp` file where youcall them all in:

```cpp
# templates.cpp
#include "SomeClass.h" // The class definition
#include "SomeClass.cpp" // Member function
template class SomeClass<type1>;
template class SomeClass<type2>'
```


### Some interesting things I learned about C++:

I did not know about destructors as this doesn't really come up in Python or Ruby. The convention is to use a `~` in front of the class name and also implement an `erase` method. However, I don't know if the `erase` method part is required or if it was just part of the tutorial I ws looking through.

I also didn't realize you could use brakcets as assignment operators. In other words `int x = 5` and `int x { 5 }` are equivalent.
