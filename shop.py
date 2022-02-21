class customer:
    def __init__(self,name,gender,age,items):
        self.name = name
        self.gender = gender
        self.age = age
        self.items = items
        self.status = False
        self.type = "n"
        self.total = 0

class smart:
    def __init__(self,clist):
        smart.clist = clist
 