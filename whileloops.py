#Input the value of terms
n = int(input("Enter the value of terms: "))

sum = 0 #initialise
i = 1 #initilialise 
while i<n: #loop will run from 1 to n
    sum = sum+i
    i = i+1
    
print("\nsum=", sum)

#infinite loop

#j = 0
#while j<=n:
#    print("I WILL RUN FOREVER")

#take input from the user
num = int(input("Enter a number: "))

#initialise sum
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
#display the results 
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number") 

#Take input from user
num1 = float(input("Please enter the first value num1: "))
num2 = float(input("PLease enter the second value for num2: "))

#calculate the HCF of user entered number
while(num2 != 0):
    temp1 = num2
    num2 = num1 % num2
    num1 = temp1

hcf = num1
#display the result
print("HCF of num1 and num2 is", hcf)

#Palindrome Numbers

#Take input from user
number = int(input("Enter a number: "))
rev = 0
#checking each digit are the same backward and forward
temp5 = num
while temp5>0:
    rem = temp5%10
    rev = rem + (rev*10)
    temp5 = (int(temp5/10))
    
#display the result 
if rev == num:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
    
#Printing a string 3 times
p = 0
while p < 3:
    print("Hello")
    p = p+1
    