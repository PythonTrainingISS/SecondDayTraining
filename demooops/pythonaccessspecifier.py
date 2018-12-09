"""
Demo for Access specifier

"""

"""
PackageManager

name
version


__init__()
get_information()
"""

class PackageManager:
    def __init__(self,name,version):
        self.__name=name ## private variable
        self.version=version

    def __get_information(self):#private method
        print('name:',self.__name)
        print('version',self.version)
    def wrapper(self):
        self.__get_information()


if __name__=='__main__':
    pm=PackageManager('pip','2.2.18')
    pm.wrapper()
    print(dir(pm))
    #print(pm.name)


