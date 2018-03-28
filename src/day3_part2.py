# Using only standard libraries
# -----------------------------

n = 200
y,x = 0,0   #Starting co-ordinates
dx = 0
dy = -1     #Starting direction
            #Change in direction follow the pattern: N-W-S-E-N
x_array = [x]
y_array = [y]
i_array = [1]

for i in range(2,n+1):
    if(x == y or (x>0 and x==1-y) or (x<0 and x==-y)): #The spiralling change direction on these 3 cases
        dy,dx = dx,-dy
    y,x = y+dy, x+dx
    y_array.append(y)
    x_array.append(x)
    sum_ = 0
    for j in range(len(y_array)-1):
        dist_x = abs(x_array[j]-x)
        dist_y = abs(y_array[j]-y)
        if dist_x <= 1 and dist_y <= 1:
            sum_ = sum_ + i_array[j]
            
    i = sum_
    i_array.append(sum_)

    if i > 265149:
        break
 
print(i_array)                
    
    
