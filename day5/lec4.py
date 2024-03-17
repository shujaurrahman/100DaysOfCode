# using for loop with range function

for number in range(1,10):
    print(number)

# range is used to check end condition in for loop upto 10 and 10 us not included 
    
for num in range(1,11,3):
    print(num)

# here iteratation is specified by the third argument numbers are printed as gap for three


# problem sum of even number till target
    target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum=0
for i in range(2,target+1,2):
  sum+=i
print(sum)