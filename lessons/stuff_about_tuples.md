[Home](../README.md)

## Tuples in C++ vs. Python

Tuples are a collection-like data structure, similar to arrays and lists. They are simply an ordered set of heterogenous items (though they contain homogenous items as well). They are often used as the data structure representation of a database record.

### Tuples in Python

In Python, suples are denoted by a collection of objects within parentheses. An example tuple in Python might look like:

```python
tup = (5, 'hello', False, 2.3)
```

Notice that the variable `tup` contains many different data types. Tuple items are accessible via the same syntax you would use to access array or list items. So grabbing the first item of a tuple would look something like:

```python
x = tup[0]
```

In the above example, the variable `x` would get the value `5` since that's the first item in `tup`.

Python tuples are immutable. This means you cannot change their value with something like

```python
tup[1] = "Hello!"
```

The above code will raise a `TypeError` with the message "'tuple' object does not support item assignment".

### Tuples in C++

C++ tuples similar to tuples in that they are made up of a collection of heterogenous objects. Due to C++ strict typing, the type and size of the tuple has to be known at compile time. Instantiating a tuple looks similar to:

```c++
std::tuple<int, char> tup1(10, 'x');
```

Unlike Python, C++ tuples are not immutable unless each data type is designated as a constant. Changing items in a C++ tuple is done like this:

```c++
std::get<0>(tup) = 100;
```

This would change the first value in `tup` to the integer `100`. If I wanted to make an exact replica of the Python tuple from the previous section, I would have to designate each item as a constant. Something like this:

```c++
std::tuple<const int, const std::string, const bool, const double> tup(5, "hello", false, 2.3)
```

Doing so makes the `tup` object immutable. The following line

```c++
std::get<0>(tup) = 100;
```
throws a compile time error.
