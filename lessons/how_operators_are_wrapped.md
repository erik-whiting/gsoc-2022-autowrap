[Home](../README.md)

## How Operators are Wrapped

Autowrap performs some magic when wrapping operators like `+`, `-`, `/`, etc or assignment operators like `+=`, `-=`, etc. This page briefly talks about how that magic works.

### Autowrap Tools Header
First, the file `autowrap/data_files/autowrap/autowrap_tools.hpp` contains template methods for the assignment operators. Here's some examples of assignment operators:

```c++
int x;
x = 10;
x += 1;
// x is now 11
x -= 2
// x is now 9
x *= 3
// x is now 27
x /= 9
// x is now 3
```

In the `autowrap_tools` header file, a template method for each assignment operator is defined. For example, the `+=` assignment operator is as follows:

```c++
template<class A> void _iadd(A * a1, const A * a2)
{
    (*a1) += (*a2);
}
```
With this `_iadd` method defined, we can now add it to the code generator.

### Code Generator
In `autowrap/CodeGenerator.py`, there's a method called `create_wrapper_for_method` which assigns the appropriate template function to the operator found. It does this by checking the operator and then returning the appropriate function. For example, the code generator `elif` block for the add assignment oeprator looks like this:

```python
 elif op == "+=":
  assert len(methods) == 1, "overloaded operator+= not supported"
  code, stubs = self.create_special_iop_method(
      "iadd", "+=", cdcl, methods[0]
  )
  return [code], stubs
```
This block first makes sure that there is only one argument passed to `+=` and raising an error otherwise. Next, it calls the `create_special_iop_method` and passes the Python name of the operator (in this case, `iadd`), the operator itself (`+=` in the above snippet), and the first method in `methods`.

### Create Special OP and IOP Method
Finally, the `create_special_iop_method` method is called in the case of assignment operators, or `create_special_op_method` otherwise. This method currently looks like this:

```python
def create_special_iop_method(self, pyname, symbol, cdcl, mdcl):
    L.info(f"   create wrapper for operator{symbol}")
    assert len(mdcl.arguments) == 1, f"operator{symbol} has wrong signature"
    ((__, t),) = mdcl.arguments
    name = cdcl.name
    assert (
        t.base_type == name
    ), f"can only apply operator{symbol} to object of same type"
    assert (
        mdcl.result_type.base_type == name
    ), f"can only return same type for operator{symbol}"
    cy_t = self.cr.cython_type(t)
    code = Code()
    code.add(
        f"""
    |
    |def __{pyname}__({name} self, {name} other not None):
    |    cdef {cy_t} * this = self.inst.get()
    |    cdef {cy_t} * that = other.inst.get()
    |    _{pyname}(this, that)
    |    return self
    """
    )

    stubs = Code()
    stubs.add(
        f"""
    |
    |def __{pyname}__(self: {name}, other: {name}) -> {name}:
    |    ...
    """
    )

    tl = Code()
    tl.add(
        f"""
            |cdef extern from "autowrap_tools.hpp":
            |    void _{pyname}({cy_t} *, {cy_t} *)
            """
    )
```
