# 30-03-2026
# 6:30PM

# Beginner level
# 1. Check even or odd
a= 18
if a%2==0:    
    print(f"{a} is Even") 
else:
    print(f"{a} is odd") 

# 2. Find largest of 3 numbers
a=19
b=17
c=18
if a>b:
    print(f"{a} is largest number.")
elif b>c:
    print(f"{b} is largest number.")
else:
    print(f"{c} is largest number.")
# 3. Check leap year.
yer=2028
if yer%4==0 or yer%400==0:
    print(f"{yer} Leap Year.")
else:
    print(f"{yer} not Leap Year.")

# 4. Check positive / negative / zero
num=1
if num<0:
    print(f"{num} is Negative Number.")
elif num>0:
     print(f"{num} is Positive Number.")
else:
     print(f"{num} is Zero Number.")
# 5. Swap two numbers (without temp)
a=10
b=20
a,b=b,a
print(f"{a}")
print(f"{b}")

#  Print 1 to N
n=7
for i in range(1,n+1):
    print(i,end=" ")
print()

# 7. Sum of first N numbers.
number=5
sum=0
for i in range(0,number+1):
    sum=sum+i
print(sum)

# 8. Factorial of a number.
numbers=5
Factorial=1
for i in range(Factorial,numbers+1):
    Factorial=Factorial*i
print(f"{numbers} Factorial is {Factorial}. ")

#  9. Multiplication table.
table=6
for i in range(1,10+1):
    print("6","X",i,"=",i*6)

# 10. Reverse a number
reverse = 4321
rev = 0
while reverse > 0:
    digit = reverse % 10          
    rev = rev * 10 + digit    
    reverse = reverse // 10           
print("Reversed number:", rev)

#  11. Star pattern (increasing). 
for i in range(1,5+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print( )
# 12. Number pattern (increasing). 
n = 5

for i in range(1, n+1):   
    for j in range(1, i+1):   
        print(j, end=" ")
    print()