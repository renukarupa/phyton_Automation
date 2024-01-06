num = int(input("Enter the number : "))
last = num%10
while num!=0:
    first = num%10
    num = num//10
sum = last+first
print("The Sum of last and first digits",sum)