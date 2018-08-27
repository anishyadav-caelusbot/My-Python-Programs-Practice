'''
Created on Apr 12, 2017

@author: Anshu
'''
import re
def main():
    fh=open('raven.txt')
    for line in fh:
        if re.search ('(len/neverm')ore'.line):
        
        print(line,end='')
main()