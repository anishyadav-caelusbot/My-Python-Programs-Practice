import sys
from pip._vendor.distlib.locators import Page

def main():
    print('Python Version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    import os 
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    
    import urllib.request
    page=urllib.request.urlopen('http://inxinfotech.com')
    print(page)
    for line in page:print(str(line,encoding='utf_8'),end='')
    
    import random
    print(random.randint(1,1000))
    
main()