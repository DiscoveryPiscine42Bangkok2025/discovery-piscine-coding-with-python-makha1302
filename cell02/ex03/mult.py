FirstNumber = int(input("Enter First Numbber : "))
SecondNumber = int(input("Enter Second Numbber : "))
Result = FirstNumber * SecondNumber
First_str = str(FirstNumber) 
Scrond_str = str(SecondNumber)
Result_str = str(Result)
if(Result < 0):
    print(First_str + " x " + Scrond_str + " = " + Result_str)
    print("This number is negative.")
elif(Result > 0):
    print(First_str + " x " + Scrond_str + " = " + Result_str)
    print("This number is positive.")
else:
    print(First_str + " x " + Scrond_str + " = " + Result_str)
    print("This number is both positive and negative.")