import sqlite3
import random
# createDb = sqlite3.connect(':memory:')
# querCursor = createDb.cursor()

def createTable():  
    try:
        db = sqlite3.connect('bank_data.db')
        qc = db.cursor()
        qc.execute('''CREATE TABLE IF NOT EXISTS ca
        (id INTEGER PRIMARY KEY,name TEXT,age INTEGER,city TEXT,state TEXT,username TEXT,password TEXT,acc_no INTEGER,amount DOUBLE)''')
        db.commit()
    except:
        print("table cant be made!")
        

class Account:
    db = sqlite3.connect('bank_data.db')
    qc = db.cursor()
        
    def __init__(self, minbalace, balance):
        self.minbalance=300
        self.balance=0

    def register(self):
        name=input("enter your name:")
        state=input("enter your state:")
        username=input("enter username:")
        age=input("enter your age:")
        password=input("enter password:")
        city=input("enter your city:")
        accno=random.randrange(100,1000000000)
        self.addCust(name,age,city,state,username,password,accno,self.balance)

    def addCust(self,name,age,city,state,username,password,accno,amount):
        self.qc.execute('''INSERT INTO ca (name,age,city,state,username,password,acc_no,amount)
        VALUES(?,?,?,?,?,?,?,?)''',(name,age,city,state,username,password,accno,amount))
        self.db.commit()
        print("successfully registered!\n")
        print("please login to continue:\n")
        x = self.qc.execute('SELECT * FROM ca WHERE username="%s"'%(username))
        for i in x:
            print("\n")
            for j in i:
                print(j)
    

    

    def login(self):
        uname=input("enter your username:")
        passw=input("enter your password:")
        j=int(input("enter the accountno to proceed:"))
        #self.db.execute('SELECT * FROM ca WHERE username=%s and password=%s'% (uname,passw))
        #print("welcome %s" % username)
        
        # db = sqlite3.connect('bank_data.db')  
        
        self.qc.execute('SELECT acc_no from ca WHERE username = "%s"'%(uname))
        # self.db.commit()  
        l = self.qc.fetchone()
        
        print(l[0]) 
        
        if l[0]==j:
             while 1:
                x=0
                print("please enter the choice for functionality!")
                print("1.to deposit amount!")
                print("2.to withdraw amount!")
                print("3.want to apply for loan!")
                print("4.see my info!")
                print("5.to exit!")
                x=eval(input("enter the no btw 1 to 4\n\n"))

                if x==1:
                    amount=eval(input("enter amount:(integer only)\n\n"))
                    self.balance+=amount
                    try:
                        self.qc.execute('''UPDATE ca SET amount = %d
                        WHERE acc_no = %d'''%(self.balance,j))
                        self.db.commit()
                        print("amount deposited successfully!")
                    except IOError:
                      print("could not update table!")
                    
                    
                        
                elif x==2:
                    amount=eval(input("enter amount:(integer only)\n\n"))
                    if self.balance-amount > self.minbalance:
                        self.balance-=amount
                        try:
                            self.qc.execute('''UPDATE ca SET amount = %d
                            WHERE acc_no = %d'''%(self.balance,j))
                            self.db.commit()
                            print("Transaction successfull!")

                        except IOError:
                                    print("could not update table!")
                    else:
                            print("sorry not enough balance u r bankrupt:)\n\n")
        
                    
                elif x==3:
                    pass
                elif x==4:
                    listitle=['Id:','Name:','Age:','City:','State:','USERNAME:','PASSWORD:','ACCOUNTNO:','BALANCE:']
                    k=0
                    c = self.qc.execute('SELECT * FROM ca WHERE acc_no=%d'%(j))
                    for i in c:
                        print("\t")
                        for j in i:
                            print(listitle[k])
                            print(j)
                            k=k+1
                            
                        
                elif x==5:break
                else:print("invalid choice!")
        else:
            print("sorry invalid accountno")

    
def run():
        a = Account(300,0)
    #ac.disp()

            #ac.dinfo()
    #po=person(300,0)
    #createDb = sqlite3.connect('bank_data.db')
    #querCursor = createDb.cursor()     
        print("WELCOME to jango BANK!\n")
        while 1:
         print("1.to register!")
         print("2.login")
         print("3.exit")
         c=eval(input("enter your choice!"))
         if c==1:
            a.register()
         elif c==2:
            a.login()
           
         elif c==3:break;
         else:print("invalid choice!")

if __name__ == '__main__':
    createTable()
    run()
