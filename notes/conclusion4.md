### Map

- map会将一个函数映射到一个输入列表的所有元素上
- map(function_to_apply, list_of_inputs)

```python
# non-map version
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

# map version
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

- 通常将map与lambda(匿名函数)配合使用
- 不仅可以用于list of values的输入，也可以用于list of functions的输入

```python
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8] 
```

### Filter
- filter过滤列表中的元素，并且返回一个由所有**符合要求**的元素所构成的列表
- **符合要求**即函数映射到该元素时返回值为True

```Python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

# Output: [-5, -4, -3, -2, -1]
```

### Reduce

- 当需要对一个列表进行一些计算并返回结果时使用reduce

```Python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
```