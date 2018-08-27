'''
Created on 30-May-2017

@author: anshu
'''
import sqlite3

def insert(db,row):
    db.execute('insert into Studata (Name,Ph_no,Rollno,Trade) values(?,?,?,?)',(row['Name'],row['Ph_no'],row['Rollno'],row['Trade']))
    db.commit()
    

    
def retrieve(db,Name):
    cursor=db.execute('select * from Studata where Name = ?',(Name,))
    return cursor.fetchone()

def update(db,row):
    db.execute('update Studata set Ph_no=? where Name=?',(row['Ph_no'],row['Name']))
    db.commit()
def delete(db,Name):
    db.execute('delete from Studata where Name=?',(Name,))
    db.commit()
def disp_rows(db):
    cursor=db.execute('select* from Studata order by Name')
    for row in cursor:
        print('{}:{}:{}:{}'.format(row['Name'],row['Ph_no'],row['Rollno'],row['Trade']))
def main():
    db=sqlite3.connect('Studata.db')
    db.row_factory=sqlite3.Row
    print('Create Table Studata')
    db.execute('drop table if exists Studata')
    db.execute('create table Studata (Name text,Ph_no int,Rollno int,Trade text)')
    
    print('Create Rows')
    insert(db,dict(Name='Rahul',Ph_no=9988671554,Rollno=8023,Trade='EE'))
    insert(db,dict(Name= 'Anish',Ph_no=9988613887,Rollno=8024,Trade='EE'))
    insert(db,dict(Name='Vivek',Ph_no=5566554556,Rollno=8025,Trade='EE'))
    insert(db,dict(Name='Karan',Ph_no=8555545664,Rollno=8026,Trade='EE'))
    disp_rows(db)
    
    print('Retrieve Rows')
    print(dict(retrieve(db,'Rahul')),dict(retrieve(db,'Anish')))
    
    print('Update Rows')
    update(db,dict(Name='Rahul',Ph_no=6936))
    update(db,dict(Name='Karan',Ph_no=8588))
    disp_rows(db)
    
    print('Delete Rows')
    delete(db,'Rahul')
    delete(db,'Vivek')
       
    disp_rows(db)
    
if __name__=="__main__": main()