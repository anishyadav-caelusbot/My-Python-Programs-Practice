def main():
    f=open('lines.txt',"r")
    for line in f.readlines():
        print(line,end='')
main()

