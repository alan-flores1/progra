num=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cont=0

for i in range (10):
    for j in range(4):
        num[i][j]=cont=cont+1
        
for i in range (10):
    print()
    for j in range (4):
        if j == 1:
            if num[i][j] < 10 :
                print (num[i][j],end="             ")
            else:
                print(num [i][j],end="           ")
        else:
            if num [i][j] < 10:
                print (num[i][j],end="      ")
            else:
                print(num[i][j],end="     ")