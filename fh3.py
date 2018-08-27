def main():
    infile=open('lines.txt','r')
    outfile=open('newfile.txt','w')
    for line in infile:
            print(line,file=outfile,end='')
main()
