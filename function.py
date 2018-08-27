value=0
try:
    with open("d:\count.bin",'r') as rr:
        value=int (rr.read())
    rr.close()
except:
    None
print value
value+=1
with open("d:\count.bin",'w') as ww:
    ww.write(str(value))
ww.close()
