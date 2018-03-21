# Only using standard libraries
#-------------------------------

data = []
with open("adv.txt","r") as f:  #Stored the input in a text file called adv.txt
  for line in f:
    data.append(line.split("\t")) #Append each line, creates a list
    
output_sum = 0
for line in data:
  line[len(line)-1] = line[-1:][0].split("\r")[0] #Split on line break chars
  output =[]
  for i in line:                                  #Max and min on each line
    output.append(int(i))
  output_sum = output_sum + max(output) - min(output)
  
print(output_sum)


# Including other libraries
#-------------------------------
import pandas as pd

data = pd.read_table("adv.txt",delimiter="\t",header = None)
print(data.head())

def max_min(row):
  return(int(max(row)-min(row)))
  
output = (data.apply(max_min,axis = 1))

print(sum((output)))
