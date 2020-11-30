class B(object):
    def __init__(self,password=''):
        self.password=password

    def lower(self):
        lower=any(c.islower() for c in self.password)
        return lower
    def upper(self):
        upper= any(c.isupper() for c in self.password)
        return upper
    def digit(self):
        digit=any(c.isdigit() for c in self.password)
        return digit
    
    def validation(self):
        lower=self.lower()
        upper=self.upper()
        digit=self.digit()
        length=len(self.password)
        cond=lower and upper and digit and length >=6 and length<=10
        if cond==True:
            print("\nUser Created Successfully\n")
        elif not lower:
            print("Include a lowerCase ")
            exit()
        elif not upper:
            print("Include a upperCase")
            exit()
        elif not digit:
            print("Include a digit")
            exit()
        elif not length>=6 and length<=10:
            print("Password length must be 6-10 characters\n ")
            exit()




class A(object):
    def __init__(self):
        pass
    print("\n\n*****WELCOME TO SMU BANKING*****\n")
    print("If you are new please create an account or Sign In with your existing account\n")
    acc=input("If you have already created and account, type 'Y' else 'N' \n")
    def Database(data,data1):
        content=open('BankingDatabase.txt','w')
        content.write(data)
        content.write(" ")
        content.write(data1)
        content.write(" ")
        content.close()
    

    def Login():
        user=input("Enter your User name\n")
        pwd=input("Enter your password\n")
        content=open('BankingDatabase.txt','r')
        L=content.readlines()
        for i in L:
            L1=i.split()
            while user and pwd not in L1:
                print("User NOT FOUND!\n")
                print("TRY AGAIN!")
                user=input("\nEnter your User name\n")
                pwd=input("Enter your password\n")

        print("\n LOGGED IN!\n Welcome "+user)
        def Transaction():
            print("\nYour Last 5 transactions\n")
            print("Date\t\t Transactions\t\t\t    Amount\n")
            print("8/11/202\t ATM w/d Kpg\t\tRs.2000")
            print("9/11/202\t Credited from Nik\t Rs.5000")
            print("10/11/202\t Electricity Bill Payed   Rs.560")
            print("8/11/202\t Paid at KFC \t\t   Rs.999")
            print("8/11/202\t Transfer to SMIT\t Rs.95000")
        def Balance():
            print("\n***ACCOUNT DETAILS***\n")
            print("Name: "+user)
            bal=int(10000)
            print("Available Balance: ",bal)
            return bal
        def Transfer():
            naam=input("Enter the Payee Name: ")
            ac=int(input("Enter the 11 Digits Account Number: "))
            amt=int(input("ENter the amount: "))
            cnf=input("Y to Pay, N to Cancel")
            if cnf=='Y':
                print("\n ---Payment Successful----\n")
                print("Payer Name: "+user)
                print("\nPayee Name: "+naam)
                print("Account Number: ",ac)
                print("Amount Paid: ",amt)
                avlbal1=Balance()
                avlbal=avlbal1-amt
                print(avlbal)
            elif cnf=='N':
                print("Transaction Cancelled!!!")
        def payment():
            ch=int(input("\n 1. Dth\n 2. Mobile\n 3. Electricty"))
            if ch==1:
                id=input("Enter your Dth No.: ")
                am=int(input("Enter the amt: "))
                cnf=input("Y to Pay, N to Cancel")
                if cnf=='Y':
                    print("\n ---Payment Successful----\n")
                    print("Id: "+id)
                    print("Amount Paid: ",am)
                    avlbal1=Balance()
                    avlbal=avlbal1-am
                    print(avlbal)
                elif cnf=='N':
                    print("Transaction Cancelled!!!")
            elif ch==2:
                id=input("Enter your Mobile No.: ")
                am=int(input("Enter the amt: "))
                cnf=input("Y to Pay, N to Cancel")
                if cnf=='Y':
                    print("\n ---Payment Successful----\n")
                    print("Id: "+id)
                    print("Amount Paid: ",am)
                    avlbal1=Balance()
                    avlbal=avlbal1-am
                    print(avlbal)
                elif cnf=='N':
                    print("Transaction Cancelled!!!")
            elif ch==3:
                id=input("Enter your Consumer No.: ")
                am=int(input("Enter the amt: "))
                cnf=input("Y to Pay, N to Cancel")
                if cnf=='Y':
                    print("\n ---Payment Successful----\n")
                    print("Id: "+id)
                    print("Amount Paid: ",am)
                    avlbal1=Balance()
                    avlbal=avlbal1-am
                    print(avlbal)
                elif cnf=='N':
                    print("Transaction Cancelled!!!")

        
        def Logout():
            print("\n LOGGED OUT SUCCESSFULLY!!!")

        choose=int(input("\nType 1: For Last Five Transactions\nType 2: View your account balance\nType 3: Pay Bills\nType 4: Money Transfer\nType 5: Logout\n"))
        while choose!=5:
            if choose==1:
                Transaction()
            elif choose==2:
                Balance()
            elif choose==3:
                payment()
            elif choose==4:
                Transfer()
            choose=int(input("\nType 1: For Last Five Transactions\nType 2: View your account balance\nType 3: Pay Bills\nType 4: Money Transfer\nType 5: Logout\n"))
            
        Logout()
        
        #choice={1:Transaction,2:Balance,3:payment,4:Transfer,5:Logout}
        #print(choice)


            #obj1=C()
            #check1=obj1.AForm()
                
        
    if acc=='Y':
        Login()
        
    elif acc=='N':
        user=input("Create a user Id\n")
        pwd=input("Create a password\n")
        obj=B(pwd)
        obj.validation()
        Database(user,pwd)
        Login()