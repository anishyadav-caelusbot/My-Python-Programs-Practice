'''
Created on Apr 14, 2017

@author: Anshu
'''
def main():
    try:
        fh=open('xlines.txt')
    except IOError as e:
        print('could not open file',e)
    else:
        for line in fh: print(line.strip())
main()