
def login(credential):
    password = credential.get('password')
    if password == None:
        
        print("Password doesn't exist")
        
    elif password== '123':
        print('login successful')
    else:
        print("Invalid login")


my_dictionary = {"username":"Jen"}
login(my_dictionary)