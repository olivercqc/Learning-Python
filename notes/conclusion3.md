### *args 和 **kwargs

- args和kwargs不是必须的，可以写成任意的变量名，但是变量名前的*和**是必须的
- *args用来发送一个非键值对的可变数量的参数列表给一个函数
- **kwargs允许不定长度的键值对作为参数传递给一个函数

```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```

```python
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

```python
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="yasoob")
```

```python
name == yasoob
```


###  可迭代对象(iterable)

- 可迭代对象就是能提供迭代器的任意对象
- 对于Python中的任意对象，需要满足一定条件才是一个可迭代对象
- 定义了一个可以返回一个迭代器__iter__方法
- 定义了可以支持下标索引的__getitem__方法
- iter将根据一个可迭代对象返回一个迭代器对象

```python
my_string = "Yasoob"
my_iter = iter(my_tsring)
next(my_iter)
# Output: 'Y'
```

### 迭代器(iterator)

- 任意对象，只要定义了next(Python2)或者__next__方法，就是一个迭代器
- next允许获取一个序列的下一个元素

```python
def generator_function():
    for i in range(3):
        yield i

gen = genrator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#StopIteration
```

### 迭代(iteration)

- 从某个**东西**中取出一个元素的过程
- 使用一个循环来遍历某个**东西**的时候，这个过程就是迭代

### 生成器(generators)

- 生成器也是一种迭代器，但是只能对其迭代一次
- 生成器并没有把所有的值存在内存中，而是在运行时生成值
- 通过遍历使用生成器, 或是用一个for循环，或是传递给任意可以进行迭代的函数和结构
- 大多数时候生成器以函数的形式来实现，并不返回一个值而是yield一个值
- 生成器占用更少的内存，当不想同一时间将计算出来的大量结果集分配到内存当中时使用

```python
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

# non-generator version
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result
```