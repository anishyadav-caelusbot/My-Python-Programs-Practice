import os
#os.mkdir('d:\hello\\fld_1\\fld_2')

for dir_n,dir_p,f_n in os.walk ('d:\hello'):
    print str(dir_n)," ",str(dir_p),"",f_n
os.rmdir("d:\hello\\fld_1")
