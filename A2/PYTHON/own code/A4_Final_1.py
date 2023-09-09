"""Hudson Xingcheng Lu              2031140
420-LCU Computer Programming, Section # 00002
S. Hilal, instructor 
Assignment 4
"""

import datetime

class BankAccount:
    Types = ["chequing", "saving", "invest", "loan", "TFSA", "RRSP"]
    Count = 0
    def __init__(self, CODE, NAME, BANK, TYPE, BALANCE=0):
    
        self.code = CODE

        #if not (8<=len(NAME)<=15):
            #print("Error")
        self.name = NAME

        #if not (2<=len(BANK)<=10):
            #print("Error")
        self.bank = BANK
        #if  (TYPE not in self.Types):
            #print("Error")
        self.type = TYPE

        #if not (0<=int(BALANCE)<=10000):
            #print("Error")
            
        self.balance = BALANCE
        self.__password = "A123456#"
        self.__last_access = datetime.datetime.now()
        BankAccount.Count += 1
        
    def __repr__(self):
        X = "{:6d} {:11s} {:6s} {:8s} {:6d} {} {}".format(self.code, self.name, self.bank, self.type, self.balance, self.__password, self.__last_access)#proper formats
        return X
    def __del__(self):
        BankAccount.Count -= 1
        #print("Deleting BankAccount instance!")
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.__last_access = datetime.datetime.now ()
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def transfer(self, code, amount):
        self.balance = self.balance - amount
        code.balance = code.balance + amount 
        return code.balance

    def verify_pwd(self,pwd):
        return self.__password == pwd

    def create_pwd(self,pwd):
        self.__last_access = datetime.datetime.now ()
   
        if(pwd.endswith("#")): #pwd[len(pwd)-1]=="#"
            if(8<=len(pwd)<=15):
                if(pwd[0].isupper()):#3
                    if (pwd.isalpha()==False):#4
                        if (pwd.isupper() == False):
                            print("Accepted")
                            self.__password = pwd
                            return pwd
                        else:
                            print("No small letters")
                    else:
                        print("no digits")
                else:
                    print("does not start with a capital letter")
            else:
                print("length does not satisfy requirements")
        else:
            print("does not end with #")


        



     ###################################to append read and close the file, after append it
          ###########################################
MyAccounts = {}   
dx = open('accounts.txt', "r")
flog=open("AccountLogs.txt","a+")


for line in dx.readlines(): 
    line = line.strip('\n')
    lines = line.split(',')
    code = int(lines[0])
    MyAccounts[code]=BankAccount(code, lines[1],lines[2], lines[3], int(lines[4]))


#for k, i in MyAccounts.items():
    #flog.write(str(i)+'\n')
    


dx.close()

menu = """

Welcome to the Bank Accounts Management App!
1- Print All Accounts (tabular format) (prints code, name, bank, acc_type, balance, last_access) 
2- Admin prints passwords and last_access of all accounts. (prints code, password, last_access) 
3- Create an account (Enter code, client name, bank name, account type and balance) 
4- Withdraw an amount from an account. (account code & amount) 
5- Deposit an amount to an account (Enter account code & amount) 
6- Transfer an amount between accounts (Enter from and to account codes and amount) 
7- Get balance of a given account (Enter account code) 
8- Update Password (request old , verify and then ask for new password) 
9- Display the log file. 
10- Exit 

Enter your requested option:"""


option = 1
while option !=11:
    option = int(input(menu))
    
    if option == 1: 
        for k in MyAccounts:
            z = str(MyAccounts[k])
            y = z.split()
            w = "{:6s} {:5s} {:6s} {:8s} {:12s} {:6d} {:6s} {}".format(y[0],y[1],y[2],y[3],y[4],int(y[5]),y[7],y[8])
            print(w)
            
    elif option == 2: 
        for k in MyAccounts:
            z = str(MyAccounts[k])
            y = z.split()
            w = "{:6s}  {:15s}  {:6s}  {}".format(y[0],y[6],y[7],y[8])
            print(w)

    elif option == 3: # 222552,John Green,RBC,chequing,0 -- dummy test

        account_info_1 = input("Enter code, client name, bank name, account type and balance:")
        lines_1 = account_info_1.split(',')
        code_1 =int(lines_1[0])                              
        MyAccounts.setdefault(code_1, BankAccount(code_1, lines_1[1],lines_1[2], lines_1[3], int(lines_1[4])))

        #flog.write(str(datetime.datetime.now())+ str(code_1)+'   created  '+'0   '+str(MyAccounts[code_1].get_balance())+'\n')  ###proper formats
        
        Z = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_1, 'Created', 0, MyAccounts[code_1].get_balance())+'\n'  
        flog.write(Z)
        
        dx.close()


    elif option == 4: 
        code_1 = int(input("Code:"))
        if code_1 in MyAccounts:
            password = input("Password verification:")
            if MyAccounts[code_1].verify_pwd(password):
                sum_1 = int(input("Amount withdrawn:"))
                if code_1 in MyAccounts:
                    MyAccounts[code_1].withdraw(sum_1)
                    TYPE = 'withdraw'
                    z = "   {:6d}   {:10s} {:6d} {:6d}".format(code_1, TYPE, sum_1,MyAccounts[code_1].get_balance() )

                Z = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_1, 'Withdraw', sum_1, MyAccounts[code_1].get_balance())+'\n'      
                flog.write(Z)
            else:
                print("Password verification fails.")
        else:
            print("Accound code does not exist.")
            break

    elif option == 5:

        code_2 = int(input("Code:"))
        if code_2 in MyAccounts:
            password = input("Password verification:")
            if MyAccounts[code_2].verify_pwd(password):
                sum_2 = int(input("Amount withdrawn:"))
                if code_2 in MyAccounts:
                    MyAccounts[code_2].deposit(sum_2)
                    TYPE = 'deposit'
                    z = "   {:6d}   {:10s} {:6d} {:6d}".format(code_2, TYPE, sum_2,MyAccounts[code_2].get_balance() )
                Z = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_2, 'Deposit', sum_2, MyAccounts[code_2].get_balance())+'\n'      
                flog.write(Z)
            else:
                print("Password verification fails.")
        else:
            print("Accound code does not exist.")
            break

    elif option == 6: 
        
        code_from = int(input("code_from:"))
        if code_from in MyAccounts:
            password = input("Password verification:")
            if MyAccounts[code_from].verify_pwd(password):
                code_to = int(input("code_to:"))
                if code_to in MyAccounts:
                    password = input("Password verification:")
                    if MyAccounts[code_to].verify_pwd(password):
                        Amount_transfer = int(input("Amount transferred:"))
                        if code_from in MyAccounts and code_to in MyAccounts:
                            MyAccounts[code_from].transfer(MyAccounts[code_to], Amount_transfer)
                        Z = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_from, 'Withdraw', Amount_transfer, MyAccounts[code_from].get_balance())+'\n'      
                        flog.write(Z)
                        Y = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_to, 'Deposit', Amount_transfer, MyAccounts[code_to].get_balance())+'\n'      
                        flog.write(Y)
                    else:
                            print("Password verification fails.")               
                else:
                    print("Accound code does not exist.")
                    break
            else:
                print("Password verification fails.")
        else:
            print("Accound code does not exist.")
            break



    elif option == 7:            
        code_3 = int(input("Code:"))
        if code_3 in MyAccounts:
            password = input("Password verification:")
            if MyAccounts[code_3].verify_pwd(password):
                if code_3 in MyAccounts:
                    MyAccounts[code_3].get_balance()
                    TYPE = 'get_balance'
                    z = "{:6d}   {:10s} {:6d}".format(code_3, TYPE, MyAccounts[code_3].get_balance() )
                    print(z)
                Z = "{}   {}   {:12s}   {:5d}   {:5d}".format(datetime.datetime.now(), code_3, 'Get Balance', 0, MyAccounts[code_3].get_balance())+'\n'      
                flog.write(Z)
            else:
                print("Password verification fails.")
        else:
            print("Accound code does not exist.")
            break




    elif option == 8: 
        code=int(input("Account code:"))
        if code in MyAccounts:
            old = input("Old password:")
            if MyAccounts[code].verify_pwd(old):
                   new = input("New password:")
                   MyAccounts[code].create_pwd(new) #working dummy: A123456a#
            else:
                print("Password verification fails.")    
        else:
            print("Accound code does not exist.")
            break

                
    elif option == 9: #9
        flog.close() # flog is the logfile object
        flog=open('AccountLogs.txt',"r")
        for line in flog:
            print(line)
        flog.close()
        flog=open('AccountLogs.txt',"a+") #ready for more logs.
        
    elif option == 10: #10
        flog.close()
        break





