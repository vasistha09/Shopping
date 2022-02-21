
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
    def __init__(self,cust):
        smart.cust = cust



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
        print(products)

