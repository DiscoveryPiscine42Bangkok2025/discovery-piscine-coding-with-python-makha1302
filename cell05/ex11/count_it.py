# Message = input("Enter Your Message : ")
# NewMessage = Message.split()
# print(f"parameters: {len(NewMessage)}")

# for i in NewMessage:
#     print(f"{i}: {len(i)}")

import sys

Message = sys.argv[1:]
if len(Message) == 0:
    print("none")
else:
    print(f"parameters: {len(Message)}")
    for i in Message:
        print(f"{i}: {len(i)}")