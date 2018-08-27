def main():
    testfun(5,6,7,8,9,10,11,one=1,two=2,three=3,four=4)
def testfun(this,that,other,*args,**kwargs):
    print('this is thest fun',kwargs['one'],kwargs['two'],kwargs['three'])
    print(this,that,other,args)
    for k in kwargs:
        print(k,kwargs[k])
main()