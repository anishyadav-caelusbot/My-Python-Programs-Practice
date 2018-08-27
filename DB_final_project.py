import sqlite3
def main():
    db=sqlite3.connect('companymaster.db')
    db.execute('drop table if exists text')
    db.execute('create table text(cccodee text,cname text,address text,P_no text)')
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('anish',23,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',())
    db.commit()
    cursor=db.execute('select* from text order by t1')
    for row in cursor:
        print(row)
main()

cccode=int(input("cccode"))