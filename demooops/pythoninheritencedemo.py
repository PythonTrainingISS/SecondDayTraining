""""
PackageManagere
name
version
init()
get_inforrmation()
^
|
ExtendedPackageManager

arch
platform

__init__()
get_Information()
"""

from demooops.pythonoopsdemo2 import  PackageManager
#import demooops.pythonoopsdemo2 as base this line of code could be used in place of "from demooops.pythonoopsdemo2 import  PackageManager"

class ExtendedPackageManager(PackageManager):
    def __init__(self,name,version,arch,platform):
        self.arch =arch
        self.platform=platform
        super.__init__(name,version)# invoking overridden method

    def get_information(self):
        super().get_information()
        print('system:',self.arch)
        print('platform',self.platform)

if __name__=='__main__':
    epm = ExtendedPackageManager('yum','2.2.18','X86_64','drawin')
    epm.get_information()


