import json,random,string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("File doesnt exist")
    except Exception as e:
        print(f"An error occured {e}")
    @classmethod
    def __generate_account_number(cls):
        alpha = random.choices(string.ascii_letters,k=4)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*~",k=2)
        id = alpha+num+spchar
        random.shuffle(id)
        return "".join(id)
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    def createAccount(self):
        info = {
            "Name" : input("Please enter your name : "),
            "Age" : int(input("Please tell your age : ")),
            "Mobile No." : int(input("Please tell your mobile number : ")),
            "Email id": input("Enter your Email id : "),
            "Account No." : Bank.__generate_account_number(),
            "Pin" : int(input("Please tell your pin : ")),
            "Balance" : 0
        }
        if info['Age'] < 18 or len(str(info['Pin'])) !=4:
            print("Sorry! Not eligible to make the bank account")
        else:
            print("Bank account created sucessfully !")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your bank account number")
            Bank.data.append(info)
            Bank.__update()
    
    def depositMoney(self):
        acc= input("Enter your account no: ")
        pin= int(input("Enter your pin: "))
        # print(Bank.data)
        customData= [i for i in Bank.data if i['Account No.']==acc and i['Pin']==pin ]
        if not customData:
            print("Sorry data not found")
            return
        else:
            print(customData[0])
            amount = int(input("Enter how much money you want to deposit: "))
            if amount >10000 or amount<=0:
                print("You can't deposit money above 10000 and below 0")
            else:
                customData[0]['Balance']+=amount
                Bank.__update()
                print("Amount deposited successfully")
    
    def withdrawMoney(self):
        acc= input("Enter your account no: ")
        pin= int(input("Enter your pin: "))
        # print(Bank.data)
        customData= [i for i in Bank.data if i['Account No.']==acc and i['Pin']==pin ]
        if not customData:
            print("Sorry data not found")
            return
        else:
            print(customData[0])
            amount = int(input("Enter how much money you want to withdraw: "))
            if amount >customData[0]['Balance'] or amount<=0:
                print(f"You can't withdraw money above {customData[0]['Balance']} and below 0")
            else:
                customData[0]['Balance']-=amount
                Bank.__update()
                print("Amount withdrawn successfully")
                print(customData[0]['Balance'])
    
    def checkDetails(self):
        acc= input("Enter your account no: ")
        pin= int(input("Enter your pin: "))
        customData= [i for i in Bank.data if i['Account No.']==acc and i['Pin']==pin]
        if not customData:
            print("Sorry data not found")
            return
        else:
            for i in customData[0]:
                print(f"{i} : {customData[0][i]}")
            print("That is all about your Bank Account")
    
    def updateDetails(self):
        acc= input("Enter your account no: ")
        pin= int(input("Enter your pin: "))
        customData=[i for i in Bank.data if i['Account No.']==acc and i['Pin']==pin]
        if not customData:
            print("Sorry data not found")
            return
        else:
            print('Before updating detials: ')
            for i in customData[0]:
                print(f"{i} : {customData[0][i]}")
            print("You cant change bank account no ,age , and balane")
            print("What you want to update in th Bank Account to update name(press 1) , mobileNo(press 2), pin(press 3)or emailId(press 4)")
            option = int(input("Enter the option : "))
            if option==1:
                print(f"Current Name: {customData[0]['Name']}")
                name = input("Enter updated name for change: ")
                customData[0]['Name']=name
            elif option==2:
                print(f"Current MobileNo: {customData[0]['Mobile No.']}")
                number = int(input("Enter updated mobileNo for change: "))
                customData[0]['Mobile No.']=number
            elif option==3:
                print(f"Current Pin: {customData[0]['Pin']}")
                temp = customData[0]['Pin']
                pin = int(input("Enter updated Pin for change: "))
                if len(str(pin)) != 4:
                    print("PIN must be 4 digits")
                    customData[0]['Pin']=temp
                else:
                     customData[0]['Pin']=pin
            elif option==4:
                print(f"Current EmailId: {customData[0]['Email id']}")
                emailId = input("Enter updated emailId for change: ")
                customData[0]['Email id']=emailId
            else:
                print("Enter correct option to update things ")
            Bank.__update()
            print('After updating detials: ')
            for i in customData[0]:
                print(f"{i} : {customData[0][i]}")

    def deleteAccount(self):
        acc= input("Enter your account no: ")
        pin= int(input("Enter your pin: "))
        customData=[i for i in Bank.data if i['Account No.']==acc and i['Pin']==pin]
        if not customData:
            print("Sorry data not found")
            return
        else:
            check = input("Press y if you actually want to delete the account or press n : ")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(customData[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()






while True:
    user = Bank()
    print("Press 1 for creating a account")
    print("Press 2 for Depositing the money in the bank account")
    print("Press 3 for withdrawing the money from the bank account")
    print("Press 4 for Details")
    print("Press 5 for updating the Details")
    print("Press 6 for deleting the Bank account")
    try:
        choice = int(input("Enter your choice : "))

        if choice ==1:
            user.createAccount()
        elif choice ==2:
            user.depositMoney()
        elif choice == 3:
            user.withdrawMoney()
        elif choice==4:
            user.checkDetails()
        elif choice == 5:
            user.updateDetails()
        elif choice == 6:
            user.deleteAccount()
        else:
            break
    except Exception as e:
        print("Please enter a valid number")
        continue