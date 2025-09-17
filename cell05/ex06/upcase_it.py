# Message = input("Enter Your Message : ")
# NewMessage = Message.split(" ")
# if(NewMessage == ['']):
#     print("none")
# else:
#     print(Message.upper())

import sys

Message = " ".join(sys.argv[1:]) 
if(Message == ""):
    print("none")
else:
    print(Message.upper())