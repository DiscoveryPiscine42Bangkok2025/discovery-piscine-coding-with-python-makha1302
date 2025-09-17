# Message = input("Enter Your Message : ")
# NewMessage = Message.split(" ")
# print(f"Number of parameters: {len(NewMessage)}.")

import sys
print(f"Number of parameters: {len(sys.argv)-1}")