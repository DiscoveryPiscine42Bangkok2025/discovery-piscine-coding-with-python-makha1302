# Message = input("Enter Your Message : ")
# NewMessage = Message.split(" ")
# if(NewMessage == [' ']):
#     print("none")
# elif(len(NewMessage) == 1):
#     print("none")
# else:
#     i = len(NewMessage)
#     while True:
#         print(NewMessage[i-1])
#         i = i - 1
#         if(i == 0):
#             break

import sys

Message = sys.argv[1:] 
if len(Message) == 0:
    print("none")
elif(len(Message) == 1):
    print("none")
else:
    i = len(Message)
    while True:
        print(Message[i-1])
        i = i - 1
        if(i == 0):
            break