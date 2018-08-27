def main() :
    func()
    hello()
    func()
    hello()
    func()
    hello()

def func():
    for i in range (10):
        print(i,end=())
        print()
def hello():
    print ('hello')
    print('welcome to function')
    main()
