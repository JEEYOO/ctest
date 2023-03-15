

hour = int(input())

count = 0
for h in range(hour+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s): #Make time to string 19:33:34 to '193334'
        count += 1
        

        
