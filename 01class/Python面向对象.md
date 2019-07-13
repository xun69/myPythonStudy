# Python面向对象

最近开始继续迷上Python，在B站视频的引领下，以及一本《Python编程从入门到实践》。

老老实实按照教科书的实例编写，发现Python的面向对象真的也挺简单的。

```python
class Dog():
    """ 这里是类的注释"""

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(self.name.title() + " is setting now")

    def roll_over(self):
        print(self.name.title() + " rolled over")

my_dog = Dog("daoge1",6)
my_dog.sit()
```

运行结果：

```shell
E:\python>python class.py
Daoge1 is setting now
```



## 子类与继承

```python
class Dog():
    """ 这里是类的注释"""

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(self.name.title() + " is setting now")

    def roll_over(self):
        print(self.name.title() + " rolled over")

class Huangdog(Dog):
    """黄狗"""

    def __init__(self,name,age):
        super().__init__(name,age)

my_dog = Huangdog("daoge1",6)
my_dog.sit()
```

## 将实例用作属性

```python
class Host():
    """狗的主人"""

    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog():
    """ 这里是类的注释"""

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.host = Host(name="xun",age=29)#将类的实例作为属性
    
    def sit(self):
        print(self.name.title() + " is setting now")

    def roll_over(self):
        print(self.name.title() + " rolled over")


class Huangdog(Dog):
    """黄狗"""

    def __init__(self,name,age):
        super().__init__(name,age)

my_dog = Huangdog("daoge1",6)
print(my_dog.host.name)
```

Dog类的`__init__`方法中使用`self.host = Host(name="xun",age=29)`指定了host属性为自定义类Host的一个实例。

## 创建与引入模块

```python
"""一个描述狗的类"""

class Host():
    """狗的主人"""

    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog():
    """ 这里是类的注释"""

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.host = Host(name="xun",age=29)#将类的实例作为属性
    
    def sit(self):
        print(self.name.title() + " is setting now")

    def roll_over(self):
        print(self.name.title() + " rolled over")

class Huangdog(Dog):
    """黄狗"""

    def __init__(self,name,age):
        super().__init__(name,age)

my_dog = Huangdog("daoge1",6)
print(my_dog.host.name)
```

通过创建模块级别的描述字符串，并且单独存储在一个.py文件中就可以当做一个Python模块了。

建立另一个文件my_dog.py:

```python
import dog
my_dog = dog.Huangdog("daoge1",6)
print(my_dog.host.name)
```

运行正常。

import dog是引入了整个dog模块。