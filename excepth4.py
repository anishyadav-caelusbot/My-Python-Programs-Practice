'''
Created on Apr 14, 2017

@author: Anshu
'''
from multiprocessing.managers import ValueProxy
from builtins import IOError
from _winapi import ReadFile
def main():
    try:
        for line in ReadFile('lines.txt'):
            print(line.strip())
    except IOError as e:
        print('cant open file',e)
    except ValueError as a:
        print('bad file name',a)
def ReadFile(fn):
    if fn.endswith('.txt'):
        fh=open(fn)
        return fh.readlines()
    else:
        raise ValueError('file must end with.txt')
main()
    