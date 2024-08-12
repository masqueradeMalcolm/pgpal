#!/bin/python3
import rsa


#make keys
def make_keys(keysize):
    (pub, priv) = rsa.newkeys(keysize)
    #decode keys into writeable pem format
    pub_pem = pub._save_pkcs1_pem().decode('utf-8')
    priv_pem = priv._save_pkcs1_pem().decode('utf-8')
    
    #write to file
    pub_file = open("public.pem", "w")
    pub_file.write(pub_pem)
    pub_file.close()

    priv_file = open("private.pem", "w")
    priv_file.write(priv_pem)
    priv_file.close()
    
    return 0


#input keysize
#run method
#make_keys(int(num))


def menu():
    while True:
        print("select an option :)")
        print("1. make keys")
        print("2. encode message")
        print("3. decode message")
        try:
            selection = int(input("type number here: "))
        except ValueError:
            print("bruh thats not even a number")
            break

        match selection:
            case 1:
                num = input("what keysize u want? ")
                make_keys(int(num))
            case 2:
                print("sorry i havent made this yet")
            case 3:
                print("sorry i havent made this yet")
            case _:
                print("invalid option dj foreskin")


menu()
