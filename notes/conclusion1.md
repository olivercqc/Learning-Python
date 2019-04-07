## Python语言特性

- 动态强类型语言
- 动态还是静态指的是编译期还是运行期确定类型
- 强类型指的是不会发生隐式类型转换

## Python作为后端语言优缺点

- 胶水语言，轮子多，应用广泛
- 语言灵活，生产力高
- 性能问题、代码维护问题、Python2/3兼容问题

## 什么是鸭子类型

> 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子


- 关注点在对象的行为，而不是类型(duck typing)
- 比如file, StringIO, socket对象都支持read/write方法(file like object)
- 再比如定义了__iter__魔术方法的对象可以用for迭代
- duck typing更关注接口而非类型

```Python
class Duck:
    def quack(self):
        print("gua gua")


class Person:
    def quack(self):
        print("我是人类，但我也会 gua gua gua")


def in_the_forest(duck):
    duck.quack()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
    print(type(donald))
    print(type(john))
    print(isinstance(donald, Duck))
    print(isinstance(john, Person))


game()


>>> gua gua
>>> 我是人类但我也会 gua gua gua
>>> <class '__main__.Duck'>
>>> <class '__main__.Person'>
>>> True
>>> True
```

### 什么是monkey patch

- 所谓的monkey patch就是运行时替换
- 比如gevent库需要修改内置的socket
- from genvent import mokey; monkey.patch_socket()

```Python
import socket
pritn(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_socket()
print("After monkey patch")
print(select.select)


import time
print(time.time())

def _time():
    return 1234

time.time = _time

print(time.time())


>>> <class 'socket.socket'>
>>> After monkey patch
>>> <class 'gevent._socket3.socket'>
>>> <built-in function select>
>>> After monkey patch
>>> <function select at 0x10b225d90>
>>> 1554607634.1482694
>>> 1234
```

### 什么是自省？

- 运行时判断一个对象的类型的能力
- Python一切皆对象, 用type, id, isinstance获取对象类型信息
- Inspect模块提供了更多获取对象信息的函数

```Python
ll = [1, 2, 3]
d = dict(a=1)

print(type(ll))
print(type(d))

print(isinstance(ll, list))
print(isinstance(d, dict))


def add(a, b):
    if isinstance(a, int):
        return a + b
    elif isinstance(a, str):
        return a.upper() + b 

print(add(1, 2))
print(add('head', 'tail'))


# 变量在内存中的地址
# 使用十进制表示地址
print(id(ll))
print(id(d))


# is判断两个变量的地址是否相同
# =判断两个变量的值是否相同
print(ll is d)
print(ll is ll)

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 == l2)
print(l1 is l2)

print(id(l1))
print(id(l2))


>>> <class 'list'>
>>> <class 'dict'>
>>> True
>>> True
>>> 3
>>> HEADtail
>>> 2620222812040
>>> 2620223655656
>>> False
>>> True
>>> True
>>> False
>>> 2620221819656
>>> 2620222726216
```

### 什么是列表和字典推导

- 比如[i for i in range(10) if i % 2 == 0]
- 一种快速生成list/dict/set的方式。用来替代map/filter等。
- (i for i in range(10) if i % 2 == 0) 返回生成器

```Python
a = ['a', 'b', 'c']
b = [1, 2, 3]
# 希望生成 d = {'a': 1, 'b': 2, 'c': 3}

d = {}
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)

d = {k: v for k, v in zip(a, b)}
print(d)

l = [i for i in range(10)]
print(l)

l = (i for i in range(10))
print(type(l))

for i in l:
    print(i)

>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
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