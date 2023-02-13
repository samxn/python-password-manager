master_pwd = input("What is the master password? ")

def view():
     with open('passwords.txt', 'r') as f:
         for line in f.readlines():
             print(line.rstrip())

def add():
    name = input('username: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view an existing password? (view/add), press q to quit. ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue