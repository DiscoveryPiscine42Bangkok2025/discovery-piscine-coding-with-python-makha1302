# import re
# Message = input("Enter Your Message : ")

# if(Message == ""):
#     print("none")
# else:
#     numbers = re.findall("z", Message)  
#     if(len(numbers) == 0):
#         print("none")
#     else:
#         for i in numbers:
#             print("z",end="")

import sys
import re

Message = " ".join(sys.argv[1:])
if len(Message) == 0:
    print("none")
else:
    numbers = re.findall("z", Message)  
    if(len(numbers) == 0):
        print("none")
    else:
        for i in numbers:
            print("z",end="")
        print()