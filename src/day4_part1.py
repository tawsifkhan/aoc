i=0
j=0
with open("adv.txt","r") as f:
  for line in f:
   j = j+1
   passphrase = []
   valid = True
   for word in line.split(" "):
     clean_word = word.split("\n")[0]
     if clean_word in passphrase:
       valid = False
       break
     else:
       passphrase.append(clean_word)
      
   if valid:
     i = i + 1
     #print(line)
   #print(line)
   #print(passphrase)
  
print(i,j)
