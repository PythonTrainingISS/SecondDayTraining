class Alpha:
    def pprint(self):
        print('pprint from class Alpha')

class Beta:
    def pprint(self):
        print('pprint from Beta class')

class Charlie(Beta,Alpha):
    def pprint(self):
        super().pprint()

if __name__=='__main__':
    Charlie().pprint()
    print(Charlie.mro())# method resolution orderobject

