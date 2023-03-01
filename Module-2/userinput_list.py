city=[]

n=int(input("Enter number of city you want:"))

for i in range(n):
    ct=input("Enter city:")
    city.append(ct)

#print(city)

for i in city:
    print(f"{city.index(i)}= {i}")