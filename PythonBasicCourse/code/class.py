class Persion:

    #初始化函数，提供属性
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    #定义方法，可以打印，返回值，处理数据
    def getlastname(self):

        if " " in self.name:
            return  self.name.split(" ")[1]
        else:
            return self.name

    def giveraise(self, percent):
        self.pay = int(self.pay*(1+ percent))

if __name__ == "__main__":
    bob  = Persion("Jack2", 10, 500)
    jack  = Persion("YouyouGao", 7, 100)

    print(bob.job)
    print(bob.name)

    bob.pay = int(bob.pay*(1+0.1))
    print(bob.pay)
    print(jack.getlastname())
    print(bob.getlastname())

    bob.giveraise(0.2)
    print(bob.pay)