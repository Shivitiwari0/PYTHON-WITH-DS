username = input("enter user name")
email = input("enter user email")
gender = input("enter user gender")
password = input("enter user password")
newpassword = input('confirm user password')

if len(username) > 4 and len(username) < 25:
    if '@' in email:
        if password == newpassword :
            print("registration done")
        else:
            print("email is incorrect")
    else:
        print("password does not match")
else:
    print("username must be between 4 and 25 chars")


