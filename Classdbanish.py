
import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'Studata3')
    
    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()
    
    def insert(self, row):
        self._db.execute('insert into {} (Name,Ph_no,Rollno,Trade) values(?,?,?,?)'.format(self._table), (row['Name'],row['Ph_no'],row['Rollno'],row['Trade']))
        self._db.commit()
    
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where Name = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())
    
    def update(self, row):
        self._db.execute(
            'update {} set Ph_no = ? where Name = ?'.format(self._table),
            (row['Ph_no'], row['Name']))
        self._db.commit()
    
    def delete(self, key):
        self._db.execute('delete from {} where Name = ?'.format(self._table), (key,))
        self._db.commit()

    def disp_rows(self):
        cursor = self._db.execute('select * from {} order by Name'.format(self._table))
        for row in cursor:
            print('  {}: {}:{}:{}'.format(row['Name'],row['Ph_no'],row['Rollno'],row['Trade']))

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by Name'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self): self.close()

    @property
    def table(self): return self._table
    @table.setter
    def table(self, t): self._table = t
    @table.deleter
    def table(self): self._table = 'Studata3'

    def close(self):
            self._db.close()
            del self._filename

def main():
    db = database(filename = 'Anishclass.db', table = 'Studata3')

    print('Create table Studata3')
    db.sql_do('drop table if exists Studata3')
    db.sql_do('create table Studata3 (Name text,Ph_no int,Rollno int,Trade text)')

    print('Create rows')
    db.insert(dict(Name='Rahul',Ph_no=9988671554,Rollno=8023,Trade='EE'))
    db.insert(dict(Name='Anish',Ph_no=9988613887,Rollno=8024,Trade='EE'))
    db.insert(dict(Name='Vivek',Ph_no=5566554556,Rollno=8025,Trade='EE'))
    db.insert(dict(Name='Karan',Ph_no=8555545664,Rollno=8026,Trade='EE'))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve('Rahul'), db.retrieve('Anish'))

    print('Update rows')
    db.update(dict(Name='Rahul',Ph_no=6936))
    db.update(dict(Name='Karan',Ph_no=8588))
    for row in db: print(row)

    print('Delete rows')
    db.delete('Rahul')
    db.delete('Anish')
    for row in db: print(row)

if __name__ == "__main__": main()
