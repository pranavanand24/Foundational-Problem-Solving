a = 12
b = 24
n = 0

for i in range(1, min(a, b)+1):
    if a%i==b%i==0:
        n+=1

print(n)