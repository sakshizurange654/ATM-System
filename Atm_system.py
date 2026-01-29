print("WELCOME TO OUR ATM SYSTEM")

atm_pin = 2004
balance = 5000

pin = int(input("enter your pin number:"))

if pin == atm_pin:
    print("you successfully enter your account")
    
    while True:
        print("\n choose following options ....")
        print("1. check your balance ")
        print("2. deposit  ")
        print("3. withdraw ")
        print("4. exit your account ...")
        
        
        choice = int(input("enter your choice :"))
        
        if choice == 1:
            print(f"your account balance is", {balance})
        
        if choice == 2:
            deposit = int(input("enter your amount :"))
            balance += deposit
            print("deposit your amount sucessfully..!!")
            print(f"{deposit}", "your is deposited")
            print(f"your total balance is : ", {balance})
            
        if choice == 3:
            withdraw = int(input("enter your amount :"))
            
            if withdraw <= balance:
                balance -= withdraw
                print(f"{withdraw}", "withdrawn your amount sucessfully..!!")
                print(f"your remaining balance is :", {balance})
            else:
                print("insufficient balance ...")
                
        if choice == 4:
            print("thank you..visit again..!!")

else:
    print("your pin is incorrect..")