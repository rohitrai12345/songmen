# Create a new list of repeated items from a provided list:
# nums = [3, 4, 2, 2, 1, 3, 3, 3]
# Output = [3, 2]
 
nums = [3, 4, 2, 2, 1, 3, 3, 3]
result=[]
for each in nums:
     if nums.count(each) > 1 and each not in result:
          result.append(each)
print(result)          

#wap to print a list of first 10 natural numbers using a for loop
result=[]
i=1
for i in range(1,10):
    result.append(i)

print(result)

#wap to print a list of even numbers using loop
even =[]
for i in range (1,11):
     if i%2 == 0:
          even.append(i) 
          print(even)

