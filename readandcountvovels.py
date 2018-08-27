'''
Created on 27-Apr-2017

@author: anshu
'''
def main():
    f=open('lines.txt',"r")
    for line in f.readlines():
        count=0
        x=0
        vowels=('a','e','i','o','u','A','E','I','O','U')
        check=0
        vowout=""
        vowin=line
        while count<x:
            if vowin in vowels:
                count+=1
                vowout=vowout+vowin
            print(vowout)
main()
