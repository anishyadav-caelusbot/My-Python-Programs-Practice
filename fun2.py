def main():
    testfun(1,2,3,43,45,45,67,77,55)
def testfun(this,that,other,*args):
    print(this,that,other,args)
    for n in args:print(n,end='')
main()