db={}

def registration(firstname,email,password):   #Function Create registration
    db["name"]=firstname
    db["email"]=email
    db["password"]=password
    print("Registration Successfully")


def login(email,password):
    if email == db["email"]:
        if password == db["password"]:
            return db["name"]
        else:
            return print("Invalid email or password")
    else:
        return print("Invalid email or password")  


menu="""
1) press 1 for reg
2) press 2 for login 
3) press 3 for exit
"""
status=True
while status:

 print(menu)

 choice = int(input("enter your choice: "))
 if choice==1:
    name=input("Enter your name : ")
    email=input("Enter your email : ")
    password=input("Enter your password : ")
    registration(name,email,password)
    

 elif choice==2:
    email=input("Enter your email : ")
    password=input("Enter your passeord")
    login(email,password)

 elif choice==3:
    status=False 
    