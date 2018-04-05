str = input("Enter String")

length = len(str)

count=0
count1=0
for i in range(0,length):
    if(str[i].isalpha()):
        count=count+1
    elif(str[i].isnumeric()):
        count1= count1+1

print("Letters : ",count)
print("Digits : ",count1)
