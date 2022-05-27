import psutil, random, array

x = array.array('i')
for i in range(1000000):
  x.insert(i, i)

for i in range(1000000):
  seed = int(random.random() * 10)
  if seed % 3:
    x[i] = int(random.random() * 10)

proc_mem = psutil.Process().memory_info().rss / (1028**2)
print(f'This process uses {round(proc_mem, 2)} MB of memory')
