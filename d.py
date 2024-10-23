n = int(input()) 

pole = []
for i in range(n):
    x = input().split()  
    pole.append([int(num) for num in x])  

for i in range(1, n):
    for j in range(1, n):
        if pole[i][j] != pole[i-1][j-1]:
            print("kopa smetia")
            exit()

print("dokonale diagonalne")
