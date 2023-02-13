pwd = input("What is the master password? ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Would you like to add a new password or view an existing password? (view/add), press q to quit").lower()
    if mode == "q":
        break
    
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode.")
        continue