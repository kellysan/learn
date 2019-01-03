#! /usr/bin/env python
# @Author : sanyapeng


str1 = "JKADFLADJFADqazwsxedcrfvtgbnhyujmkilophnfgsdfgsgsdacshsfasdgvscxgsaxbssedacghqtXDFZGCSVZOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOADOGAOFUOWTEJCXAJVOASFIOAJODFJOAHFIHAFJVADPSJVAJNOFJAOSJFA"
dict1 = {}
set1 = set(str1)
#print(set1)

for i in set1:
    count = 0
    for j in str1:
        if i == j:
            count += 1
        dict1[i] = count

for k,v in dict1.items():
    print(k,v)

print('-'* 100)

dict2 = {}
for i in str1:
    if i not in dict2:
        dict2[i] = 1
    elif i in dict2:
        dict2[i] += 1
for k,v in dict2.items():
    print(k,v)

print('-'* 100)
dict3 = {}
for i in str1:
    count = dict3.get(i)
    if count == None:
        dict3[i] = 1
    else:
        dict3[i] += 1
for k,v in dict3.items():
    print(k,v)