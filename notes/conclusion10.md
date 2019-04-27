### 枚举(enumerate)

- enumerate允许我们遍历数据并自动计数

```Python
for counter, value in enumerate(some_list):
    print(counter, value)
```

- enumerate也接受一些可选参数

```Python
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
```

- 上面的参数允许我们指定从哪个数字开始枚举
- 也可以用来创建包含索引的元组列表