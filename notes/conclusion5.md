### set

- set与列表类似 但是不能包含重复的值

```Python 
# 检查列表中是否包含重复元素

# for loop versison
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in deplicates:
            deplicates.append(value)

print(duplicates)

# Output: ['b', 'n']

# set version
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# Output: set(['b', 'n'])
```

```Python
# intersection 
# 比较两个集合的交集
valid = ste(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

#Output: set(['red'])
```

```Python
# difference
# 找出两个集合的差集
valid = ste(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# Output: set(['brown'])
```

### 三元运算符(条件表达式)
- 在一行内进行快速的判断，避免复杂的多行if语句

```Python
# condition_is_true if condition else condition_is_false
is_fat = True
state = "fat" if is_fat else "not fat"
```