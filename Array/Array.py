from array import *

# val = array('i',[1,2,3,4,5,6]) 

# val.insert(1,50)
# val.append(100)

''' for i in range(0,len(val)):
    print(val[i] , end =" ")

print('\n')
 
for x in val:
    print(x, end = ' , ')

print('\n')

# print(val.typecode)

# val.reverse()

# for i in range(0,len(val)):
    # print(val[i] , end = ' ') '''

''' copyArray = array(val.typecode, (x*3 for x in val)) 

copyArray.pop(3)

for i in range(0,len(copyArray)):
    print(copyArray[i] , end = ' ') '''

# sliing methode

val = array('i',[1,2,3,4,5,6,7,8,9])

abc = val[:: -1]

print(abc)

