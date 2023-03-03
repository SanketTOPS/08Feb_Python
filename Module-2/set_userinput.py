data=[]

n=int(input("Enter number of data:"))

for i in range(n):
    x=input("Enter data:")
    data.append(x)

print(data)
print(set(data))