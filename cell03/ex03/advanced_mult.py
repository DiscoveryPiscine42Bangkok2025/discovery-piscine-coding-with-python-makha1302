i = 0
while True:
    print(f"Table de {i} : ",end="") 
    j = 0
    while True:
        print(f"{i*j} ",end="")
        j = j + 1
        if(j == 10):
            break
    if(i == 10):
        break
    print("")
    i = i + 1