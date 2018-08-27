import re
def main():
    fh=open('raven.txt')
    pat=re.compile('(len/neverm)ore',re.i)
    for line in fh:
        if re.search(pat.line):
            print(pat.sub('###',line),end=")
main()