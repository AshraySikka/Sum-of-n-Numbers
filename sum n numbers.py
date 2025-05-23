n=int(input("Enter the number of Numbers you want to add: "))
sum=0
while n!=0:
    num=int(input('Enter number: '))
    sum=sum+num
    n-=1
print("sum of all the numbers: ", sum)
