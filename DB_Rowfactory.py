'''
Created on 30-May-2017

@author: anshu
'''
import sqlite3
def main():
    db=sqlite3.connect('text.db')
    db.row_factory=sqlite3.Row
    db.execute('drop table if exists text')
    db.execute('create table text(t1 text,i1 int,t2 text,t3 text)')
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('anish',23,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.execute('insert into text (t1,i1,t2,t3) values (?,?,?,?)',('rahul',24,'real','work'))
    db.commit()
    cursor=db.execute('select* from text order by t1')
    for row in cursor:
        print(row)
main()