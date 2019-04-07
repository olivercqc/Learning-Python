## Python2/3差异

### Python3改进1

- print成为函数
- 编码问题. Python3不在有Unicode对象, 默认str就是Unicode
- 除法变化. Python3除号返回浮点数

### Python2

```Python
print 'b'
print('a', 'b')

s = u'中文'
print(type(s))

print 5/2


>>> b
>>> ('a', 'b')
>>> unicode
>>> 2
```

### Python3

```python
print('b')
print('a', 'b', sep='|')

s = '中文'
print(type(s))

def 大写(s):
    return s.upper()
大写('abc')

print(s)
print(s.encode())
print(type(s.encode()))

print(5/2)
print(5//2)


>>> b
>>> a|b
>>> str
>>> 'ABC'
>>> 中文
>>> b'\xe4\xb8\xad\xe6\x96\x87'
>>> <class 'bytes'>
>>> 2.5
>>> 2
```

### Python3改进2

- 类型注解(type hint). 帮助IDE实现类型检查
- 优化的super()方便直接调用父类函数
- 高级解包操作. a, b, *rest = range(10)

### Python2

```python
class Base(object):
    def hello(self):
        print("hello")


class C(Base):
    def hello(self):
        return super(C, self).hello()


c = C()
c.hello()


a, b, c = [1, 2, 3]
print a, b, c


>>> hello
>>> 1 2 3
```

### Python3

```python
def hello(name: str) -> str:
    return 'hello ' + name
print(hello('laocao'))

class Base(object):
    def hello(self):
        print("hello")

class C2(Base):
    def hello(self):
        return super().hello()


c2 = C2()
c2.hello()

a, b, *c = range(10)
print(a)
print(b)
print(c)

a, b, *_ = range(5)
print(a)
print(b)


>>> hello laocao
>>> hello
>>> 0
>>> 1
>>> [2, 3, 4, 5, 6, 7, 8, 9]
>>> 0
>>> 1
```

### Python3改进3

- Keyword only arguments. 限定关键字参数
- Chained exceptions. Python3重新抛出异常不会丢失栈信息
- 一切返回迭代器(iterators) range, zip, map, dict.values, etc.

### Python2

```python
print range(10)


>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Python3

```python
def add(a, b, c):
    return a + b + c


print(add(1, 2, 3))


# 限定关键字参数需要指定参数名传参
def add(a, b, *, c):
    return a + b + c


print(add(1, 2, c=3))


import shutill


def mycopy(source, dest):
    try:
        shutil.copy2(source, dest)
    except OSError:
        raise NotImplementedError("automatic sudo injection") from OSError


mycopy('old', 'new') 


print(range(10))
for i in range(10):
    print(i)
>>> 6
>>> 6
>>> range(0, 10)
>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9
```

### Python3新增

- yield from 链接子生成器
- asyncio内置库, async/await原生协程支持异步编程
- 新的内置库enum, mock, asyncio, ipaddress, concurrent.futures等

### Python3改进4

- 生成的pyc文件统一放到__pycache__
- 一些内置库的修改. urllib, selector等
- 性能优化

### 兼容Python2/3的工具

- six模块
- 2to3等工具转换代码
- future
