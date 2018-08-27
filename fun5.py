def main():
    for i in testfun(0,25,3):
        print(i,end='')
def testfun(start,stop,step):
    i=start
    while i<stop:
        yield i
        i+=step
main()