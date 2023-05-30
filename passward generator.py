import random
import string

def pass_generate(pw_len):

    passwords = [] 

    for i in pw_len:
        
        password = "" 
        characters = string.ascii_letters + string.digits
        for j in range(i):
            password += (random.choice(characters))     
        passwords.append(password) 
    
    return passwords

def main():
    
    num_pass = int(input("Enter the number of passwards you want :- "))
    pw_len = []

    for i in range(num_pass):
        length = int(input("Enter the length of Password " + str(i+1) + " :- "))
        pw_len.append(length)
    print("\n")

    Password = pass_generate(pw_len)
    for i in range(num_pass):
        print ("Password number "+str(i+1)+" :- " + Password[i])

main()