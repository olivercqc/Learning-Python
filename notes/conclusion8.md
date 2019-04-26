## global and return

- global变量意味着可以在函数以外的区域都能访问这个变量
- return将函数计算得到的值返回给调用它的变量

```Python
# return version add
def add(value1, value2):
    return value1 + value2

result = add(3, 5)
print(result)
# Output: 8


# non-global version add
def add(value1, value2):
    result = value1 + value2

add(3, 5)
print(result)
# Output: NameError: name 'result' is not defined


# global version add
def add(value1, value2):
    global result
    result = value1 + value2

add(3, 5)
print(result)
# Output: 8
```

- 尽量避免使用global关键字 引入了多余变量到全局作用域


### mutation

- 将一个变量赋值为另一个可变类型的变量时
- 对这个数据的任意改动会反映到这两个变量上去
- 新变量是对老变量的一个别名 (只针对可变数据类型)

```Python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']

print(foo)
# Ouput: ['hi', 'bye']
# Expected output: ['hi']

print(bar)
# Output: ['hi', 'bye']
```

- 在Python中当函数被定义时 默认参数只会运算一次 而不是每次被调用时都会重新运算
- 最好不要定义可变类型的默认参数

```Python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]
# Expected output: [1]

add_to(2)
# Output: [1, 2]
# Expected output: [2]

add_to(3)
# Output: [1, 2, 3]
# Expected output: [3]


def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
```

### __slots__

- 默认情况下Python用一个字典来保存一个对象的实例属性
- 这一特性允许我们在运行时去设置任意的新属性
- 对于有着已知属性的小类来说 这一特性会浪费很多内存
- 应该在对象创建时直接分配一个固定量的内存来保存所有的属性
- 可以使用__slots__来告诉Python不要使用字典 而且只给一个固定的属性分配空间

```Python
# non-slots version
class MyClass(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.setup()
    # ...

# slots version
class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.setup()
    # ...     
```