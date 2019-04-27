### collections

### defaultdict

- Python中的 **词典(dict)** 由"键"(key)进行索引(常表示为 **dict(key:val, ...)** )
- dict有以下特点
- key可以是不可变(immutable)数据类型(数字, 字符串, 元组)不可为列表和字典
- 每个键必须是唯一的
- 字典中每一项的顺序是任意的
- defaultdict是dict类的一个子类 会为不存在的键提供默认值 避免了KeyError

```Python
# KeyError version
bag = ['apple', 'orange', 'cherry', 'apple', 'cherry', 'blueberry']
count = {}
for fruit in bag:
    count[fruit] += 1

print(count)
# Output: 'apple'

# defaultdict version
from collections import defaultdict
bag = ['apple', 'orange', 'cherry', 'apple', 'cherry', 'blueberry']
count = defaultdict(int)
for fruit in bag:
    count[fruit] += 1

print(count)
# Output: defaultdict(<class 'int'>, {'apple': 2, 'orange': 1, 'cherry': 2, 'blueberry': 1})
```

- 避免了在字典中对一个键嵌套赋值时的KeyError

```Python
import json

# KeyError version
some_dict = {}
some_dict['colors']['favorite'] = 'yellow'

print(json.dumps(some_dict))
# Output: KeyError: "colors"

# defaultdict version
from collections import deafultdict
tree = lambda: defaultdict(tree)
some_dict = tree()
some_dict['colors']['favorite'] = 'yellow'

print(json.dumps(some_dict))
# Output: {"colors": ["favorite": "yellow"]}
```

### counter

- 计数器 可以准队某项数据进行计数

```Python
from collections import Counter

avengers = (
    ('tony', 'red'),
    ('tony', 'yellow'),
    ('cap', 'blue'),
    ('wakanda', 'black'),
)

favs = Counter(name for name, color in avengers)
print(favs)
# Output: Counter({'tony': 2, 'cap': 1, 'wakanda': 1})
```

- 可以用来统计一个文件

```Python
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

### deque

- 双端队列 可以在头/尾添加或者删除元素

```Python
from collections import deque

d = deque()

# 提供了与 list 类似的方法
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# OuputL 3

# 可以从两端 取出 (pop) 数据
d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: 0

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])

# 可以从任一端拓展队列中的数据
d = deque([1, 2, 3, 4, 5])
d.extendleft([0])
d.extend([6, 7, 8])
print(d)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])

# 可以限制 deque 的 maxlen 当超过设定的限制时 数据会从队列另一端挤出去
d = deque(maxlen = 30)
# 此时当插入30条数据时 最左边的数据将从队列删除
```

### namedtuple

- 元组(tuple)是一个不可变的列表 可以存储一个数据的序列
- 元组中的数据是不可修改的
- 为了获取元组中的数据 需要使用整数作为索引

```Python
man = ('tony', 42)
print(max[0])
# Output: tony
```

- namedtuple将元组变成一个针对简单任务的容器
- 可以像字典一样访问namedtuple 而不必使用整数索引
- namedtuple是不可变的

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'
```
- namedtuple有两个必须的参数 元组名称和字段名称
- 使用namedtuple可以兼容普通的元组 既可以用整数索引 也可以用名称来访问namedtuple

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')

print(perry[0])
# Output: perry
```

- 可以将一个namedtuple转换为dict

```Python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')

print(perry._asdict())
# Output: OrderedDict([('name', 'perry'), ('age', 31), ('type', 'cat')])
```
