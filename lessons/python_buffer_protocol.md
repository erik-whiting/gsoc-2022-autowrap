[Home](../README.md)

## The Python Buffer Protocol (basics)

The buffer protocol in Python gives a way to directly access the contents in memory of an object. This is useful when working with large objects such as a multi-dimensional array one migh find when doing image processing.

When copying data from one object to another, Python will often make a copy of one of the objects, increasing memory usage. However, with direct access to the contents of memory, we can avoid this unnecessary use of space. This is why the memory buffer protocol is useful.

As an example, consider the two scripts:

This one uses Python lists
```python
import psutil, random

x = []
for i in range(100000):
  x.append(i)

for i in range(100000):
  seed = int(random.random() * 10)
  if seed % 3:
    x[i] = int(random.random() * 10)

proc_mem = psutil.Process().memory_info().rss / (1028**2)
print(f'This process uses {round(proc_mem, 2)} MB of memory')
```

This one uses Python array (and thus the buffer protocol):
```python
import psutil, random, array

x = array.array('i')
for i in range(100000):
  x.insert(i, i)

for i in range(100000):
  seed = int(random.random() * 10)
  if seed % 3:
    x[i] = int(random.random() * 10)

proc_mem = psutil.Process().memory_info().rss / (1028**2)
print(f'This process uses {round(proc_mem, 2)} MB of memory')
```

On average, the process using Python lists uses approximately 18 MB of memory, whereas the process using Python arrays (which use the buffer array protocol and thus skip copying memory) only uses 14 MB of memory. This is a small difference but suppose we make the loops one more order of magnitude higher. Then, the process with lists uses approximately 53 MB whereas the process using arrays hovers around 18 MB. This indicates that arrays scale better for this kind of solution.
