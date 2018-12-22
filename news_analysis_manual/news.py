import matplotlib.pyplot as plt

#INDIAN EXPRESS DEC 21
dict1={'To ease their cash crunch Govt to put in Rs.83000crore in public sector banks':'Economics',

'2 tributaries increasing Ganga pollution load: Report':'Environment',

'Never fall in love on FB,I wasted 6 years':'Social Media',

'Witnesses allege mismanagement by prosecution,seek to be re-examined':'Justice',

'At 4C Capital,sees its coldest morning in four years':'Climate'}

key1 = list(dict1)  
#print(key1)
#print("\n")
temp1 = dict1.values()
val1 = list(temp1)  
#print(val1)


#TIMES OF INDIA DEC 21

dict2={'Loan Waiver Pledge Causes 24% rise in MP farm NPAs':'Economics',

 'Homi Bhabha cluster univ gets cabinet nod':'Education',
 
 'GPS device on Western Railway to track trains on mishap relief duty':'Technology',
 
 'Toll 11 as lung patient, week-old girl succumb to their injuries':'Medicine',
 
 'SC: Don’t deny legal aid to accused in court martial': 'Justice'}
#print("\n")
key2 = list(dict2)  
#print(key2)
#print("\n")
temp2 = dict2.values()
val2 = list(temp2)  
#print(val2)
 
#DECCAN CHRONICLE DEC 21

dict3={'Set for Takeoff,Vision drives TN Education towards the future':'Education',

 'Sneaking out of sabha concerts':'Cultural',
 
 'Good samaritans utilise social media for gaja relief':'Environment',
 
 'Best Engineer award for Krishnamoorthy in Trichy' : 'Education',
 
 'Rockets too hard for Wizards':'Sports'}

#print("\n")
key3 = list(dict3)  
#print(key3)
#print("\n")
temp3 = dict3.values()
val3 = list(temp3)  
#print(val3)

print("INDIAN EXPRESS:")
print("\n")
print(dict1)
print("\n")

print("TIMES OF INDIA:")
print("\n")
print(dict2)
print("\n")

print("DECCAN CHRONICLE:")
print("\n")
print(dict3)
print("\n")

print("Domains Highlighted:")
print("\n")
val=val1+val2+val3
print(val)

print("\n")
from collections import Counter
a = dict(Counter(val))
print("Domain counts:")
print(a)

keys= list(a)  
temps = a.values()
vals = list(temps)  
#print(keys)
#print(vals)

figureObject, axesObject = plt.subplots()
axesObject.pie(vals,
        labels=keys,
		autopct='%1.2f',
        startangle=90)

# Aspect ratio - equal means pie is a circle
axesObject.axis('equal')
plt.show()









