user_data=[42,7,108,2026,88,9,1337]
  even_digit_count=0
for number in user_data:
  digit_count=len(str(abs(number)))
    if digit_count%2==0:
       even_digit_count+=1
pint(f"Simulated UserData:{user_data}")
print(f"Number of items with an even number :{even_digit_count}")
