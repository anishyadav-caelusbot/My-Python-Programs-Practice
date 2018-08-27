def main():
    testfun(44,33,32)
    testfun(36,49)
    testfun(22)

def testfun(num,anothernum=None,onemore=88):
    if anothernum is None:
        anothernum=0
    print('this is test ',num,anothernum,onemore)
main()
    
        