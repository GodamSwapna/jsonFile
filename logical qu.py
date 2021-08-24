with open("1.txt","w") as f:
    i=0
    sum=0
    while i<30:
        input1=int(input("enter a number:"))
        str1=str(input1)+"\n"
        f.write(str1)
        sum+=input1
        i+=1
    f.write(str(sum))
    print("total income spendin:",sum)
    
