string=input("Enter string:")
count1=0
count2=0
count3=0
count4=0
count5=0

for i in string:
      if(i.isdigit()):
            count1=count1+1
      elif(i.isalpha()):
            count2=count2+1
            if(i.isupper()):
                count3 = count3+1
            if (i.islower()):
                count4 = count4 + 1
      else:
          count5 = count5+1

print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)
print("The number of uppercase letters is:")
print(count3)
print("The number of lowercase letters is:")
print(count4)
print("The number of special characters is:")
print(count5)