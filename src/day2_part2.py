# Only using standard libraries
# ------------------------------
data = []
with open("adv.txt","r") as f:
  for line in f:
    data.append(line.split("\t")) #Append each line, creates a list
    
output =[]
  
for line in data:
  line[len(line)-1] = line[-1:][0].split("\r")[0] #Split on line break chars
  for i in range(len(line)-1):
    prev = int(line[i])
    for j in range(i+1,len(line)):
      next = int(line[j])
      if prev%next == 0 or next%prev==0:
        print(prev,next, int(max(prev,next)/min(prev,next)))
        output.append(int(max(prev,next)/min(prev,next)))

print(sum(output))
  
