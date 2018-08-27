'''
Created on Apr 14, 2017

@author: Anshu
'''
try:
    fh=open('lines.txt')
    for line in fh.readlines():
        print(line)
        
except IOError as e:
        print('something bad happend({})'.format(e))
print("after badness")
        