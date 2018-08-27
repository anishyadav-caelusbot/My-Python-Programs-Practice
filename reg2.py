import re
def main():
    fh=open('raven.txt')
    for line in fh:
        match=re.search('(len/neverm)ore'.line)
        if match:
            print(match.group)
main()
