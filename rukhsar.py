s1=int(input("Enter marks:"))
s2=int(input("Enter marks:"))
s3=int(input("Enter marks:"))
s4=int(input("Enter marks:"))

if s1>40 and s2>40 and s3>40 and s4>40:

    total=s1+s2+s3+s4
    pr=total/4
    print(total)
    print(pr)
    if total>70:
        print("Distinction")
    elif total>60:
        print("first class")
    elif total>50:
        print("second class")
    elif total>40:
        print("pass class")
else:
        print("Fail")
