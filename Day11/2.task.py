# WAP to delete all the occurrences of a specified character in a given string 
# S = “All the occurrences of a specified character in a given string”
# Input = “a”
# Output = “ll occurrences of  specified chrcter in  given string”

S = "All the occurrences of a specified character in a given string"
char = input("enter the character you want to remove")
result =""
for each in s:
    if each == char :
        continue
    result += each
    print(result)

# Check whether a number is palindrome or not
# a = 121
# Output = “It is a palindrome number”
# A = 321
# output = “It is not a palindrome number”
    
    num=input("enter a number")
    if num ==num[::-1]:
        print("it is palindrome")
    else:
        print("it is not a palindrome")

        num = int(input("Enter a number "))
temp = num
summ = 0

while num != 0:  # 321
    r = num % 10  # 1  2  3
    summ = summ * 10 + r  # 123
    num = num // 10  # 0
    
if temp == summ:
    print("It is palindrome")
else:
    print("It is not palindrome")

