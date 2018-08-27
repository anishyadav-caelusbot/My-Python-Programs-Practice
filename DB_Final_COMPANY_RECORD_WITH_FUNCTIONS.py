'''
Created on 30-May-2017

@author: anshu
'''


import sqlite3  

def insertcm(db,row):
    db.execute('insert into Company_master (cccode,C_name,C_address,C_Phone) values(?,?,?,?)',
               (row['cccode'],row['C_name'],row['C_address'],row['C_Phone']))
    db.commit()
    
def insertim(db,row):
    db.execute('insert into Item_master (item_code,cccode,Item_name,Item_UNIT) values(?,?,?,?)',
               (row['item_code'],row['cccode'],row['Item_name'],row['Item_UNIT']))
    db.commit()

def insertsm(db,row):
    db.execute('insert into Stock_master (Stock_code,item_code,Quantity) values(?,?,?)',
               (row['Stock_code'],row['item_code'],row['Quantity']))
    db.commit()
    
def inserttt(db,row):
    db.execute('insert into Trans_table (Trans_id,item_code,Quantity,Trans_type,Trans_Date) values(?,?,?,?,?)',
               (row['Trans_id'],row['item_code'],row['Quantity'],row['Trans_type'],row['Trans_Date']))
    db.commit()    
    
def joincm_im(db):
    cursor=db.execute('SELECT Company_master.cccode, Item_master.item_code FROM Company_master INNER JOIN Item_master ON Company_master.cccode=Item_master.cccode')
    return cursor.fetchone()

def joinim_sm(db):
    cursor=db.execute('SELECT Item_master.item_code, Stock_master.Stock_code FROM Item_master INNER JOIN Stock_master ON Item_master.item_code=Stock_master.item_code')
    return cursor.fetchone()

def joinsm_tta(db):
    cursor=db.execute('SELECT Stock_master.Stock_code, Trans_table.Trans_id FROM Stock_master INNER JOIN Trans_table ON Stock_master.item_code=Trans_table.item_code')
    return cursor.fetchone()

def joinsm_ttb(db):
    cursor=db.execute('SELECT Stock_master.Stock_code, Trans_table.Trans_id FROM Stock_master INNER JOIN Trans_table ON Stock_master.Quantity=Trans_table.Quantity')
    return cursor.fetchone()    
    
def retrieve(db,cccode):
    cursor=db.execute('select * from Company_master where cccode = ?',(cccode,))
    return cursor.fetchone()

def updateqwtm(db,row):
    db.execute('update Trans_table set Quantity=? where item_code=?',(row['Quantity'],row['item_code']))
    db.commit()
    
def updatepwcc(db,row):
    db.execute('update Company_master set C_Phone=? where cccode=?',(row['C_Phone'],row['cccode']))
    db.commit()
    
def updateqwim(db,row):
    db.execute('update Item_master set Quantity=? where item_code=?',(row['Quantity'],row['item_code']))
    db.commit()
    

def updateqwsm(db,row):
    db.execute('update Stock_master set Quantity=? where Stock_code=?',(row['Quantity'],row['Stock_code']))
    db.commit()
    
def deletecc(db,cccode):
    db.execute('delete from Company_master where cccode=?',(cccode,))
    db.commit()
    
def deleteim(db,cccode):
    db.execute('delete from Item_master where cccode=?',(cccode,))
    db.commit()
    
def deletesm(db,cccode):
    db.execute('delete from Stock_master where cccode=?',(cccode,))
    db.commit()
    
def deletett(db,cccode):
    db.execute('delete Trans_table where cccode=?',(cccode,))
    db.commit()
    
def disp_rowscm(db):
    cursor=db.execute('select* from Company_master order by cccode')
    #print ('Company code: Comapny Name: Comapny Address: Company Phone')
    for row in cursor:
        print('Company code:{}  Comapny Name:{}  Comapny Address:{}  Company Phone:{}'.format(row['cccode'],row['C_name'],row['C_address'],row['C_Phone']))
        
def disp_rowsim(db):
    cursor=db.execute('select* from Item_master order by cccode')
    #print ('Item Code : Company code: Item Name: Item Unit')
    for row in cursor:
        print('Item Code : {}  Company code : {}  Item Name : {}  Item Unit : {}'.format(row['item_code'],row['cccode'],row['Item_name'],row['Item_UNIT']))

def disp_rowssm(db):
    cursor=db.execute('select* from Stock_master order by Stock_code')
    #print ('Stock code : Item code: Quantity')
    for row in cursor:
        print('Stock code : {}  Item code : {}  Quantity : {}'.format(row['Stock_code'],row['item_code'],row['Quantity']))
        
def disp_rowstt(db): 
    cursor=db.execute('select* from Trans_table order by Trans_id')
    #print ('Transaction ID : Item code: Quantity: Transaction Type (S/P): Transaction Date ')
    for row in cursor:
        print('Transaction ID : {}  Item code: {}  Quantity : {}  Transaction Type (S/P) : {}  Transaction Date : {}'.format(row['Trans_id'],row['item_code'],row['Quantity'],row['Trans_type'],row['Trans_Date']))
        
def show_tables(db):
    cursor=db.execute('show tables')
    return cursor.fetchone()

def main():
    
          
    db=sqlite3.connect('Stockmaster.db')
    db.row_factory=sqlite3.Row
    print('------------------------------Welcome to Stock Master Database--------------------------------')
    print('----------------------------------------------------------------------------------------------')
    print('----------------------------------Company_master Table----------------------------------------')
    #db.execute('drop table if exists Company_master')
    #db.execute('create table Company_master (cccode text,C_name text,C_address text,C_Phone text)')
    #print('Create Rows')
    disp_rowscm(db)
    #insertcm(db,dict(cccode=(input("Enter company code")),
                  # C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                   #C_Phone=(input("Enter company Phone no"))
                  # ))
   # insertcm(db,dict(cccode=(input("Enter company code")),
                  # C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                  # C_Phone=(input("Enter company Phone no"))
                   #))
    #insertcm(db,dict(cccode=(input("Enter company code")),
                   #C_name=(input("Enter company name")),
                  # C_address=(input("Enter company Address")),
                  # C_Phone=(input("Enter company Phone no"))
                   #))
    #insertcm(db,dict(cccode=(input("Enter company code")),
                   #C_name=(input("Enter company name")),
                   #C_address=(input("Enter company Address")),
                   #C_Phone=(input("Enter company Phone no"))
                   #))
    #disp_rowscm(db)
    
   
    #item master______________________________________________________________________________________________________
    
    print('----------------------Item Master Table----------------------')
    #db.execute('drop table if exists Item_master')
    #db.execute('create table Item_master (item_code text,cccode text,Item_name text,Item_Unit text)')
    #print('Create Rows')
    disp_rowsim(db)
    #insert(db,cccode,C_name,C_address,C_Phone)
    #insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
    
    #insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                  # Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
   # insertim(db,dict(item_code=(input("Enter Item code")),
                  # cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                  # ))
    #insertim(db,dict(item_code=(input("Enter Item code")),
                   #cccode=(input("Enter company code")),
                   #Item_name=(input("Enter Item Name")),
                   #Item_UNIT=(input("Enter Item UNIT"))
                   #))
   
   
   
    joincm_im(db)
    
    
    #Stock Master______________________________________________________________________________________________________
    
    
    
    print('------------------------Stock Master Table---------------------')
    disp_rowssm(db)
    #db.execute('drop table if exists Stock_master')
    #db.execute('create table Stock_master (Stock_code text,item_code text,Quantity text)')
    #print('Create Rows')
    #insert(db,cccode,C_name,C_address,C_Phone)
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
    #               item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
    #               ))
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
   #                item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
     #              ))
    #insertsm(db,dict(Stock_code=(input("Enter Stock code")),
    #               item_code=(input("Enter Item code")),
    #               Quantity=(input("Enter Quantity")),                   
     #              ))
   # insertsm(db,dict(Stock_code=(input("Enter Stock code")),
      #             item_code=(input("Enter Item code")),
      #             Quantity=(input("Enter Quantity")),                   
          #         ))
        
    
    
    
    joinim_sm(db)
    #Transaction______________________________________________________________________________________________________
    
    
    print('----------------------Transaction Table--------------------------')
    disp_rowstt(db)
    #db.execute('drop table if exists Trans_table')
    #db.execute('create table Trans_table (Trans_id text,item_code text,Quantity text,Trans_type text,Trans_Date text)')
    #print('Create Rows')
    #insert(db,cccode,C_name,C_address,C_Phone)
    #inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
     #              item_code=(input("Enter Item code")),
     #              Quantity=(input("Enter Quantity")),
      #             Trans_type=(input("Enter Transaction Type: S / P")),
     #              Trans_Date=(input("Enter Transaction Date"))
      #             ))
    
    #inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
          #        item_code=(input("Enter Item code")),
           #        Quantity=(input("Enter Quantity")),
             #      Trans_type=(input("Enter Transaction Type: S / P")),
              #     Trans_Date=(input("Enter Transaction Date"))
              #     ))
    
   # inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
          #         item_code=(input("Enter Item code")),
                #   Quantity=(input("Enter Quantity")),
                  # Trans_type=(input("Enter Transaction Type: S / P")),
                  # Trans_Date=(input("Enter Transaction Date"))
                  # ))
    
    #inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
         #          item_code=(input("Enter Item code")),
                 #  Quantity=(input("Enter Quantity")),
                  # Trans_type=(input("Enter Transaction Type: S / P")),
                #   Trans_Date=(input("Enter Transaction Date"))
                 #  ))
    
    
    joinsm_tta(db)
    joinsm_ttb(db)
    
    #print('Retrieve Rows')
    #print(dict(retrieve(db,'Rahul')),dict(retrieve(db,'Anish')))
    
    
    
    
    
    
    #_____________________________________________________________________________________
    #to Modify 
    #______________________________________________________________________________________
    
    print('For Add 1 ,  For Update Press 2, For Delete Press 3 , For Exit Press 4')

    v=(input("From 1 to  4"));
    
    #add values
    
    if v=='1':
        print('Insert/Add New values in Tables')
        print('For Company Master #Press a ,  For Item Master $Press b, For Stock Master #Press c , For Transaction Table #Press d')
        print('Select Table to Add Values')
        f=(input("From a to d"));
        if f=='a':
            print('Company Master Selected - Add Values')
            insertcm(db,dict(cccode=(input("Enter company code")),
                   C_name=(input("Enter company name")),
                   C_address=(input("Enter company Address")),
                   C_Phone=(input("Enter company Phone no"))
                   ))
            print('Values Added to Company Master')
            
        if f=='b':
            print('Item Master Selected - Add Values')
            insertim(db,dict(item_code=(input("Enter Item code")),
                   cccode=(input("Enter company code")),
                   Item_name=(input("Enter Item Name")),
                   Item_UNIT=(input("Enter Item UNIT"))
                   ))
            print(' Values Added to Item Master')
            
        if f=='c':
            print('Stock Master Selected - Add Values')
            insertsm(db,dict(Stock_code=(input("Enter Stock code")),
                   item_code=(input("Enter Item code")),
                   Quantity=(input("Enter Quantity")),                   
                   ))
            print(' Values Added to Stock Master ')
        if f=='d':
            print('Transaction Table Selected - Add Values')
            inserttt(db,dict(Trans_id=(input("Enter Transaction ID")),
                   item_code=(input("Enter Item code")),
                   Quantity=(input("Enter Quantity")),
                   Trans_type=(input("Enter Transaction Type: S / P")),
                   Trans_Date=(input("Enter Transaction Date"))
                   ))
            print(' Values Added to Transaction Table')
        else:
            print('Invalid Input #Enter a Value Between a to d #')
        
        
    #update
    
        
    if v=='2':
        print('Update values in Tables')
        print('For Company Master #Press a ,  For Item Master $Press b, For Stock Master #Press c , For Transaction Table #Press d')
        print('Select Table to Add Values')
        g=(input("From a to d"));
        if g=='a':
            print('Company Master Selected - Update Values')
            updatepwcc(db,dict(C_Phone=(input("Update New Company Phone No.")),cccode=(input("Enter Company Code to Update Phone no."))))
            print('Company Master Updated')
            
        if g=='b': 
            print('Item Master Selected - Update Values')
            updateqwim(db,dict(Quantity=(input("Enter Updated Quantity")),item_code=(input("Enter Item Code to Update Quantity"))))
            print('Item Master Updated')
         
        if g=='c':
            print('Stock Master Selected - Update Values')
            updateqwsm(db,dict(Quantity=(input("Enter Updated Quantity")),item_code=(input("Enter Item Code to Update Quantity"))))
            print('Stock Master Updated')
        
        if g=='d':
            print('Transaction Table Selected - Update Values')
            updateqwtm(db,dict(Quantity=(input("Enter Updated Quantity")),item_code=(input("Enter Item Code to Update Quantity"))))
            print('Stock Master Updated')
    
    
    
    #delete
    
         
    if v=='3':
        print('Delete values in Tables')
        print('For Company Master #Press a ,  For Item Master $Press b, For Stock Master #Press c , For Transaction Table #Press d')
        print('Select Table to Delete Values')
        h=(input("Select table From a to d"));
        if g=='a':
            print('Company Master Selected - Delete Values')
            deletecc(db,'Rahul')
        if g=='b':
            print('Item Master Selected - Delete Values')
            deleteim(db,'Rahul') 
        if g=='c':   
            print('Stock Master Selected - Delete Values') 
            deletesm(db,'Rahul')
        if g=='d':
            print('Transaction Table Selected - Delete Values')
            deletett(db,'Rahul') 
            
    if v=='4':
        print(' v is ofne')
    else:
        print('Invalid Input #Enter a Value Between 1 to 4 #')
    
    
    #update(db,dict(cccode='Karan',C_name=8588))
    #disp_rows(db)p
    #print('Update Company Master')
    
        
    #print('Update Transaction Table')
    
    #print('Delete Rows')
    #delete(db,'Rahul')
    #delete(db,'Vivek')
       
    #disp_rows(db)
    #print('Enter Action')
    #updateqwtm(db)
    
    
    

main()