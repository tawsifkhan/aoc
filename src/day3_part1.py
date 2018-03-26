
# Only using standard libraries
# ------------------------------

n = 265149
y,x = 0,0   #Starting co-ordinates
dx = 0
dy = -1     #Starting direction
            #Change in direction follow the pattern: N-W-S-E-N

for i in range(2,n+1):
    if(x == y or (x>0 and x==1-y) or (x<0 and x==-y)): #The spiralling change direction on these 3 cases
        dy,dx = dx,-dy
    y,x = y+dy,x+dx
    
print(y,x,i)
print(abs(y)+abs(x))
