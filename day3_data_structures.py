nums=list(map(int,input("Enter the numbers:").split()))
sum=0
max=nums[0]
min=nums[0]
for num in nums:
 sum=sum+num
 if(num>max):
  max=num
 if(num<min):
  min=num
print(f"Sum:{sum}")
print(f"Max:{max}")
print(f"Min:{min}")
#frequency
freq={}
for num in nums:
  if num in freq:
    freq[num]+=1
  else:
   freq[num]=1
print(f"Frequencies:{freq}")
#reverse
reverse_num=[]
for i in range(len(nums)-1,-1,-1):
  reverse_num.append(nums[i])
print(f"Reversed List:{reverse_num}")
