user = input("enter your username")
password = input("enter your password")

if user == "Admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("invalid password")
else:
    print("invalid username")
