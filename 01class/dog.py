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