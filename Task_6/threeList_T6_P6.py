sets = [[1,2,3], [3,4,5], [5,6,1]]
seen = set()
duplicates = set()

for subset in map(set, sets) :
     duplicates |= (subset & seen)
     seen |= subset

print("The duplicate number in three list are : ",duplicates)

