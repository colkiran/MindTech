
def outerFun(fnc):
    def helperFun(amt):
        print("logging into the server.....")
        fnc(amt)
        print("logged out of the server......")
        print("-" * 60)

    return helperFun

@outerFun               # deposit = outerFun(deposit)
def deposit(amt):
    print(f"Credited {amt} into Account ending with xxxx")

deposit(50000)


@outerFun
def withdraw(amt):
    print(f"Debited {amt} from the Account ending with xxxx")

withdraw(15000)

