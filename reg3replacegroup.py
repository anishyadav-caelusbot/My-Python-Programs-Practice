
import re
def main():
    print('hello')
    fh=open('raven.txt')
    for line in fh:
        match=re.search('(len/neverm')ore.line)
        if match:
            print (line.replace(match.group(),'***'),end='')
            
        
main()