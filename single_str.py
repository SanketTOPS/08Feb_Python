str1=input("Enter First String:")
str2=input("Enter Second String:")

x=str1[0:2]

a=str1.replace(str1[0:2],str2[-2:])
b=str2.replace(str2[-2:],x)

print(a,b)






