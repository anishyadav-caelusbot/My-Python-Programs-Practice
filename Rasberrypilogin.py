def main():
    choices={'name':'anish','userid':'23'}
    v='anish'
             
    print(choices.get(v,'RasberryPi Login')) 
    name=int(input("Enter your id--"))   
    if name==23:
        fh=open('line.txt')
        for line in fh.readlines():
            print(line)
    
    else:
        print('Please Enter correct Username')
main()    