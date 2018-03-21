#Part One
#-------------------------------------------
input = "91212129"
input = input + input[0] #Make it circular

next = []
prev = input[0]
match = []

for i in range(len(input)-1):
  next = input[i+1]
  if next == prev:
    match.append(int(next))
  
  prev = next
  
print(sum(match))

#Part Two
#-------------------------------------------
input = "12131415"
steps = int(len(input)/2)  #Input is even always

input = input + input[0:steps] #Make it circular upto halfway
next = []
prev = input[0]
match = []

for i in range(len(input)-steps):
    prev = input[i]
    next = input[i+steps]
    if next == prev:
        match.append(int(next))
  
print(sum(match))
