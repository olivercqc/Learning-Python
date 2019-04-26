### 装饰器 Decorator

```Python
# 从 Python 中的函数开始 
def hi(name="olivercqc"):
    return "hi" + name

print(hi())
# Output: "hi olivercqc"

# 可以将函数赋值给一个变量
greet = hi
print(greet())
# Output: "hi olivercqc"

# 现在删除旧的 hi 函数
del hi
print(hi())
#Output: NameError

print(greet())
#Output: "hi olivercqc"
```

```Python
# 可以在一个函数中定义另一个函数
# 即可以创建嵌套的函数
def hi(name="olivercqc"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"
    
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()

# Output: 
# now you are inside the hi() function
# now you are in the welcome() function
# now you are in the welcome() function
# now you are back in the hi() function

greet()
# Output: NameError: name 'greet' is not defined

# greet() 和 welcome() 函数在 hi() 函数之外是不能访问的
```

```Python
def hi(name="olivercqc"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "olivercqc":
        return greet
    else:
        return welcome

a = hi()
print(a)
# Outputs: <function hi.<locals>.greet at 0x000001BEF46F90D0>
print(a())
# Outputs: now you are in the greet() function

# 将一对小括号放到函数后面，函数就会执行
# 如果不放括号在函数后面，那么函数就可以被到处传递，并且可以赋值给别的变量而不去执行它
a = hi(name = "zyc")
print(a())
# Outputs: now you are in the welcome() function
print(hi()())
# Outpus: now you are in the greet() function
```

```Python
# 将函数作为参数传给另一个函数
def hi():
    return "hi olivercqc!"

def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)
# Outputs:
# I am doing some boring work before executing hi()
# hi olivercqc!
```

```Python
# decorator
def a_new_decorator(a_func):

    
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    
    
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
# Outputs: I am the function which needs some decoration to remove my foul smell

a_function_requiring_decoration = a_new_decorator
(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction

a_function_requiring_decoration()
# outpus:
# I am doing some boring work before executing a_func()
# I am the function which needs some decoration to remove my foul smell
# I am doing some boring work after executing a_func()

# 装饰器封装一个函数，并且通过某种方式修改它的行为
```

```Python 
# 可以使用 @ 符号来生成一个被装饰的函数
# 现在使用 @ 来运行之前的代码
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration():
# outpus:
# I am doing some boring work before executing a_func()
# I am the function which needs some decoration to remove my foul smell
# I am doing some boring work after executing a_func()

# @a_new_decorator 仅仅是一种简写
''' 是对 a_function_requiring_decoration = a_new_decorator
(a_function_requiring_decoration) 的简写 '''
```

```Python
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
```

- 此时函数被 *wrapTheFunction* 替代了， 重写了原函数的名字和docstring
- 可以使用functools.wraps来解决

```Python
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before excuting a_func()")
        a_func()
        print("I am doing some boring work after excuting a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
```
