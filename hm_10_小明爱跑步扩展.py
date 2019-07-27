class Person:

    def __init__(self, name, weight):
        # self.属性 = 跑步
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步, 跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 爱吃东西, 小明是吃货" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美", 45)

xiaomei.eat()
xiaomei.run()

print(xiaomei)
print(xiaoming)
