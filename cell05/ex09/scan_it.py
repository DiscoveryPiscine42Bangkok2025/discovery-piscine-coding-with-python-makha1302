# import re

# MainMessage = input("Enter Your Main Message : ")
# Message = input("Enter Your Messafe : ")
# if(MainMessage == "" or Message == ""):
#     print("none")
# else:
#     numbers = re.findall(MainMessage, Message)      
#     print(len(numbers))

import sys 
import re

if (len(sys.argv) < 3): 
    print("none")
else:
    MainMessage = sys.argv[1] 
    Message = " ".join(sys.argv[2:])
    if(MainMessage == "" or Message == ""):
        print("none")
    else:
        numbers = re.findall(MainMessage, Message)      
        print(len(numbers))
