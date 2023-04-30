usernameInput = input("User :")
passwordInput = input("Pass :")

if usernameInput == "xxxx"  and passwordInput == "xxxx" :
    print("Sucess!!")
    print("-----------------------")
    print("-----Mxke Gun Shop-----")
    print("-----------------------")
    print("1. Glock 17 Gen 5 : 87,000 thb")
    print("2. Glock 19 Gen 5 : 85,000 thb")
    print("3. Glock 26 Gen 3 : 65,000 thb")
    print("4. Glock 26 Gen 4 : 88,000 thb")
    userSelected = int(input("Select >>"))
    if userSelected == 1:
        glock17g5 = int(input("How Many? :"))
        print("Price of Glock17 Gen5 :",glock17g5*87000,"thb")
    elif userSelected == 2:
        glock19g5 = int(input("How Many? :"))
        print("Price of Glock19 Gen5 :",glock19g5*85000,"thb")
    elif userSelected == 3:
        glock26g3 = int(input("How Many? :"))
        print("Price of Glock26 Gen3 :",glock26g3*65000,"thb")
    elif userSelected == 4:
        glock26g4 = int(input("How Many? :"))
        print("Price of Glock26 Gen4 :",glock26g4*88000,"thb")
    print("Thank")

else:
    print("Wrong Username or Password!!!")
