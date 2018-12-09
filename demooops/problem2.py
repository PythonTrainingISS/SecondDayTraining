class Product:
    def __init__(self,pid):
        self.pid = pid

    def __str__(self):
        return '{} #id:{}'.format(self.__class__.__name__,self.pid)

    #__repr__=__str__

class Cart:
    def __init__(self):
        self.cart=Product(123)
    def add(self,p):
        self.cart.append(p)

    def __str__(self):
        return '{} contains = {}'.format(self.__class__.__name__,self.cart)

if __name__=='__main__':
    c=Cart();
    print(c)