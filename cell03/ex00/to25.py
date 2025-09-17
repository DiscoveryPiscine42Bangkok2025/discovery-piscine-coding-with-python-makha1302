Number = int(input("Enter Number : "))
if (Number > 25):
    print("Error")
else:
    while True :
        print(f"Inside the loop, my variable is {Number}")
        if (Number == 25) :
            break 
        Number = Number + 1