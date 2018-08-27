def main():
    buffersize=50000
    infile=open('bigfile.txt','r')
    outfile=open('newbigfile.txt','w')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
    print()
    print('Done')
main()
