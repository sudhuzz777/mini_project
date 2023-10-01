pwd = input("what is the the master password? ")

def view():
    pass

def add():
    name = input('Account Nmae: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
       f.write(name + "|" + pwd)

       

while True:
   mode = input("would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
   if mode == "q":
       break

   if mode == "view":
        view()
   elif mode == "add":
        add()  
   else:
       print("invalid mode.")
       continue 