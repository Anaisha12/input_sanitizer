import string
username = input("Username: ")
password = input("Password: ")
i=0
if("\'" in username):
    while i<len(username):
        if(username[i]=='\''):
            username=username[0:i]+username[i+1:len(username)]
        i=i+1
i=0
if("\'" in password):
    while i<len(password):
        if(password[i]=='\''):
            password=password[0:i]+password[i+1:len(password)]
        i=i+1
if(username[-1]=='\\'):
    username=username[0:len(username)-1]
if(password[-1]=='\\'):
    password=password[0:len(password)-1]    
print(username+"\n")
print(password+"\n")