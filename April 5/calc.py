x = int(input("Enter first number"))
y = int(input("Enter second number"))

if x > y:
    greater = x
else:
    greater = y

while (True):
    if ((greater % x == 0) and (greater % y == 0)):
        lcm = greater
        break
    greater += 1

print("LCM : ",lcm)

if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
        hcf = i

print("HCF : ",hcf)

print("Factors of ",x)
for i in range(1,int(x/2) +1):
    if(x % i == 0):
        print(i,end='')

print("\nFactors of ",y)
for i in range(1,int(y/2) +1):
    if(y % i == 0):
        print(i,end='')