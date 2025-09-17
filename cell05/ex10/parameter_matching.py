# MessagePassword = input("Enter Your Key Password : ")
# Message = input("What was the parameter? ")
# if(MessagePassword == "" or Message == ""):
#     print("none")
# elif(Message == MessagePassword):
#     print("Good job!")
# else: 
#     print("Nope, sorry...")

import sys

if (len(sys.argv) < 3): 
    print("none")
else:
    MainMessage = sys.argv[1] 
    Message = " ".join(sys.argv[2:])
    if(MainMessage == "" or Message == ""):
        print("none")
    elif(Message == MainMessage):
        print("Good job!")
    else: 
        print("Nope, sorry...")