# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:30:29 2020

@author: Necro
"""

X=[(4, 3), 'West', 1, [(5, 3), 'South', 1, [(5, 4), 'South', 1, ((5, 5), None, 0)]]]
#X=[ ((4, 3), 'West', 1), [((5, 3), 'South', 1), [((5, 4), 'South', 1), [((5, 5), None, 0), None]] ] ]
#[(((5, 3), 'South', 1), (((5, 4), 'South', 1), (((5, 5), None, 0), None)))]
Y=[]
#X=list(X)
#popitemlist=
while True:
    #X=list(X)
    
    popitem=X.pop()
    print(popitem)
    
    print('after pop:',X,len(X))
    
    Y.append(X[1])
    #X=list(popitem)
    print(popitem)
    #X=list(popitem)
    if len(popitem)==0:
        break
    X=list(popitem)

print(Y)

#print(popitem)