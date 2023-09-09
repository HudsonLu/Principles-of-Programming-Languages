"""Hudson Xingcheng Lu              2031140
420-LCU Computer Programming, Section # 
S. Hilal, instructor 
Lab 11
"""



import datetime

class BankAccount:
    Types = ["chequing", "saving", "invest", "loan", "TFSA", "RRSP"]
    Count = 0
    def __init__(self, CODE, NAME, BANK, TYPE, BALANCE=0):
    
        self.code = CODE

        if not (8<=len(NAME)<=15):
            print("Error")
        self.name = NAME

        if not (2<=len(BANK)<=10):
            print("Error")
        self.bank = BANK
        if  (TYPE not in self.Types):
            print("Error")
        self.type = TYPE

        if not (0<=int(BALANCE)<=10000):
            print("Error")
            
        self.balance = BALANCE
        self.__password = "123"
        self.__last_access = datetime.datetime.now()
        BankAccount.Count += 1
        
    def __repr__(self):
        X = "{:6d} {:11s} {:6s} {:8s} {:6d}".format(self.code, self.name, self.bank, self.type, self.balance)#proper formats
        return X
    def __del__(self):
        BankAccount.Count -= 1
        print("Deleting BankAccount instance!")
    
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


    def create_pwd(self):
        self.__last_access = datetime.datetime.now ()
        if (pwd.isalnum()):
            if(pwd.endswith("#")): #pwd[len(pwd)-1]=="#"
                if(8<=len(pwd)<=15):
                    if(pwd[0].isupper()):#3
                        if (pwd.isalpha()==False):#4
                            if (pwd.isupper() == False):
                                print("accepted")
                                self.__password = pwd
                            else:
                                print("no small letters")
                        else:
                            print("no digits")
                    else:
                        print("does not start with a capital letter")
                else:
                    print("length does not satisfy requirements")
            else:
                print("does not end with #")
        else:
            print("all except last character not alphanumeris")
        return self.pdw


   #main code

MyAccounts = {}   
dx = open('accounts.txt', "r") 

for line in dx.readlines(): 
    line = line.strip('\n')
    lines = line.split(',')
    code = int(lines[0])
    MyAccounts[code]=BankAccount(code, lines[1],lines[2], lines[3], int(lines[4]))
 


account_info_1 = "122156,Lea Smith,TD,saving,200"
account_info_2 = "222552,John Green,RBC,chequing,0"
lines_1 = account_info_1.split(",")
lines_2 = account_info_2.split(",")

code_1 =int(lines_1[0])
code_2 =int(lines_2[0])
                          
MyAccounts.setdefault(code_1, BankAccount(code_1, lines_1[1],lines_1[2], lines_1[3], int(lines_1[4])))
MyAccounts.setdefault(code_2, BankAccount(code_2, lines_2[1],lines_2[2], lines_2[3], int(lines_2[4])))

#MyAccounts['122156']=BankAcount(int(acc[0]),acc[1],acc[2],acc[3],int(acc[4])
#a1 = BankAccount(int(122156), "Lea Smith", "TD", "saving", int(200))
#a2 = BankAccount(int(222552), "John Green", "RBC", "chequing", int(0))


dx.close()  

################

            #deposit 100$ in account ID 122156

code = 122156
#for code in MyAccounts:
if code in MyAccounts:
    MyAccounts[122156].deposit(100)



            #deposit 100$ in account ID 888888
code_1 = 888888
if code_1 in MyAccounts:
    MyAccounts[888888].deposit(100)


    

             #getbalence

code = 122156
if code in MyAccounts:
    MyAccounts[122156].get_balance()


             #transfer
code_from = 122156
code_to = 222552

if code_from in MyAccounts and code_to in MyAccounts:
    MyAccounts[122156].transfer(MyAccounts[222552], 50)


for k in MyAccounts:
    print(MyAccounts[k])



  



