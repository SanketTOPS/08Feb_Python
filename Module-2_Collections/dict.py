stdata={'id':101,'name':'sanket','sub':'python'}
print(stdata)
"""print(stdata['sub'])
print(stdata.get('name'))
print(len(stdata))"""
#print(stdata.keys())
#print(stdata.values())

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

"""stdata['id']=102
print(stdata)"""

"""if 'sanket' in stdata.items():
    print("Yes...")
else:
    print("Noo")"""

stdata["city"]="rajkot"
#stdata.pop('name')
#del stdata['sub']
#stdata.clear()
print(stdata)

newdict=stdata.copy()
print(newdict)