city=['rajkot','baroda','surat','ahmedabad']

"""print(city[0])
print(city[-1])
print(city[0:3])
print(city[2:])
print(city[:2])"""

#print(len(city))
#city[1]="navsari"
#print(city)

"""for i in city:
    print(i)"""

#print(city.index('surat'))

#0 rajkot
#1 baroda

"""for i in city:
    print(f"{city.index(i)}={i}")"""

"""if "junagadh" in city: #membership operator
    print("Yes...")
else:
    print("Noo")"""

# ---------------------------------------------------------- #
print(city)
#city.append("navsari")
#city.insert(2,"junagadh")
#city.remove('surat')
#city.pop()
#city.pop(1)
#city.clear()
#del city[1]
#del city
#print(city)

#newcity=city.copy()
#print(newcity)

newcity=['bhavnagar','jamnagar','morbi']
#print(newcity)

#print(city+newcity)
#city.extend(newcity)
#print(city)

#city.reverse()
city.sort()
print(city)