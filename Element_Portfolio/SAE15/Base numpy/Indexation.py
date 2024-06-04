#Indexation simple

import numpy as np
#uneRangee = np.empty((7,4), dtype=int)
#print(uneRangee)

#Indexation booléenne

#tabNotes = np.array([10,8,14,7,6,11,18,6,9,20])
#print(tabNotes[tabNotes >= 10])
#print(tabNotes >= 10)

#tabNotes2d = np.array([[12,5,7],[8,18,6],[11,13,20]])
#print(tabNotes2d)
#print(tabNotes2d < 10)
#print(tabNotes2d[tabNotes2d <= 10])
#print(tabNotes2d[tabNotes2d[:,2]<=10])

uneLigne1d = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(uneLigne1d[np.array([[17,18,19],[0,1,2]])])