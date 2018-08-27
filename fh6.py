def main():
    buffersize=50000
    infile=open('olives.jpg','r')
    outfile=open('newimg.jpg','wb')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end='')
        buffer=infile.read(buffersize)
    print()
    print('done')
main()
