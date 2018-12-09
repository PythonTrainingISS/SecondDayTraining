import  os
import  pprint

class SystemInformation:
    def __init__(self):#constructor
        print(self,'am constructor')

    def __del__(self):
        print(self,'getting destroyed')

   # pass## dummy code block
if 1==1:
    pass# its a python keyword used to define dummy code block

if __name__ == '__main__':
    print(__name__)# to check namespace of a script
    print()
    si = SystemInformation()
    print(si)
    print()
    print(SystemInformation)
    print(os.__name__)
    print(pprint.__name__)

