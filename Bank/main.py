import sqlite3
conn = sqlite3.connect("Bank.db")
cursor = conn.cursor()


# cursor.execute('''
# create table Account(
#                name varchar(32) not null,
#                phone number(10) check(length(phone=10)),
#                aadhar number(12) check(length(aadhar=12)) not null unique,
#                dob date not null,
#                address varchar(100) not null,
#                acc_no integer primary key AUTOINCREMENT,
#                gender varchar(7),
#                pin number(4) default(0),
#                amount number(8,2),
#                acc_type varchar(10) not null
#                )
# ''')

# cursor.execute(f"insert into Account(name, phone,aadhar,dob,address,acc_no,gender,acc_type,amount) values('Sameera',7998102094,123456789012,'24-02-2004','1-2-116',1200,'female','saving',500)")
# conn.commit()



def acc_creation(name,phone,dob,aadhar,address,gender,acc_type):
    cursor.execute(f"insert into Account (name,phone,dob,aadhar,address,gender,acc_type,amount) values('{name}','{phone}','{dob}','{aadhar}','{address}','{gender}','{acc_type}',500)")
    conn.commit()
    print('acc created successfully')



def pin_generation(acc,pin,c_pin):
    if pin == c_pin:
        cursor.execute(f"update Account set pin = {pin} where acc_no = {acc}")
        conn.commit()
        print("Successfully set pin, don't share with anyone...")
    else:
        print("confirm pin doesnt match...")




def balance(acc,pin):
    data = cursor.execute(f"select * from Account where acc_no = {acc}")
    result = data.fetchone()

    if pin == result[-3]:
        print(f"balance is {result[-2]}")
    else:
        print("Invalid pin")



def deposite(acc,pin):
    data = cursor.execute(f"select * from Account where acc_no = {acc}")
    var = data.fetchone()


    if pin == var[-3]:
        amt = float(input("Enter the amount :"))
        if amt >= 100 and amt<=10000:
            money = var[-2]
            cursor.execute(f"update Account set amount = {amt+money} where acc_no = {acc}")
            conn.commit()
            print("your deposite is successfully done")
        elif amt < 100:
            print('minimum deposite must be 100 rupees...')
        else:
            print('maximum deposite must be 10000 rupeess')
    else:
        print("invalid pin...")


def withdrawl(acc,pin):
    data = cursor.execute(f"select * from Account where acc_no = {acc}")
    var = data.fetchone()

    if pin == var[-3]:
        amt = float(input("Enter the amount"))
        money = var[-2]
        if amt >= 100 and amt <= money:
            cursor.execute(f"update Account set amount = {money-amt} where acc_no = {acc}")
            conn.commit()
            print("Your withdrawl is successfully done")

        elif amt <100:
            print("your withdrawl must be 100 rupees..")
        else:
            print("insufficient balance...")
    else:
        print("invalid pin")


def transfer(from_acc,to_acc,pin):
    data = cursor.execute(f"select * from Account where acc_no = {from_acc}")
    from_account = data.fetchone()


    if pin == from_account[-3]:
        amt = float(input("Enter the Amount :"))
        if amt>= 100 and amt <= 10000:
            if from_account[-2] >= amt:
                cursor.execute(f"update Account set amount = {from_account[-2]-amt} where acc_no = {from_acc}")
                conn.commit()

                data1 = cursor.execute(f"select * from Account where acc_no = {to_acc}")
                to_account = data1.fetchone()
                cursor.execute(f"update Account set amount ={to_account[-2]+amt} where acc_no = {to_acc}")
                conn.commit()
                print("Amount successfully transfered..")
            else:
                print("insufficiant balance...")
        else:
            print("invalid amount")
    else:
        print("invalid pin")

user_input = int(input('''
                        \n Welcome to SBI
                        \n choose the below option
                        \n 1)Account creation
                        \n 2)Pin Creation
                        \n 3) Balance Enquiry
                        \n 4) Deposite
                        \n 5) Withdraw
                        \n 6) Account Transfer
                       '''))



if user_input == 1:
    print("Thank you for choosing our bank:")
    name = input("Enter your name:")
    dob = input("Enter your DOB:")
    phone = int(input("Enter your mobile number: "))
    address = input("Enter your address:")
    aadhar = int(input("Enter your aadhar number :"))
    gender = input("Enter your gender:")
    acc_type = input("what is your account type...")
    acc_creation(name,phone,dob,aadhar,address,gender,acc_type)

elif user_input == 2:
    print("=========================Generate your pin=======================")
    acc = int(input("Enter your account number:"))
    pin = int(input("Enter your pin:"))
    c_pin = int(input("Confirm pin:"))
    pin_generation(acc,pin,c_pin)


elif user_input == 3:
    print("================Balance Enquiry==========")
    acc = int(input("Enter your account number:"))
    pin = int(input("Enter your pin"))
    balance(acc,pin)

elif user_input == 4:
    print("==================DEPOSITE===============")
    acc = int(input("Enter your account number:"))
    pin = int(input("Enter your pin :"))
    deposite(acc,pin)

elif user_input == 5:
    print('=============================Withdrawl==============================')
    acc = int(input("Enter your account number :"))
    pin = int(input("Enter your pin :"))
    withdrawl(acc,pin)


elif user_input == 6:
    print("=============Amount Transfer==================")
    from_acc = int(input("Enter the senders account number :"))
    to_acc = int(input("Enter the receivers account number :"))
    pin = int(input("Enter your pin"))
    transfer(from_acc,to_acc,pin)

else:
    quit()