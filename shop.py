
from pickle import TRUE


class customer:
    def __init__(self,name,gender,age,items):
        self.name = name
        self.gender = gender
        self.age = age
        self.items = items
        self.status = "False"
        self.type = "n"
        self.total = 0

class smart:
    def __init__(self,cust):
        smart.cust = cust

def check(cust):
    for c in cust:
        sum =0
        for p in c.items:
            sum = sum+c.items[p]
        c.total = sum
        if(c.age>=50 and sum>=500 ):
            c.type = "f"

def disc(cust):
    for c in cust:
        if (c.type=="f" and c.total<=1000 ):
            c.total = c.total - c.total*0.1
            c.status = "true"
        elif(c.total>1000 and c.total<2500):
            c.total = c.total - c.total*0.15
            c.status = "true"
        elif(c.total>=2500):
            c.total = c.total - c.total*0.25
            c.status = "true"
        print("{} total amount = {} discount status {}".format(c.name,c.total,c.status))

        

    




if __name__=="__main__":
    cust = []
    no_of_cust = int(input())
    for i in range(no_of_cust):
        name = input()
        gender = input()
        age = int(input())
        n_items = int(input())
        products = {}
        for i in range(n_items):
            item = input()
            price = int(input())
            products.update({item:price})
        cust.append(customer(name,gender,age,products))
    check(cust)
    disc(cust)
    
    


