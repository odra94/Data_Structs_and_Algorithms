
aList = [0,9,8,7,6,5,4]

aList.append(8)

print("Length of aList: " + str(len(aList)))

print("Ranged for-loop from 0 to len(aList):")
for index in range(1, len(aList)):
    print(aList[index],index)

print("Removed number 6 from list")
aList.remove(6) # Remove item with value 6 from list

print("Enumarated for-loop of list: (index,item):")
for index, item in enumerate(aList):
    print(index,item)

print("Popped last item of list and saved it.")
itemToInsert = aList.pop() # Remove last item from list and return it

print("Inserted the popped item at the front of the list.")
aList.insert(0,itemToInsert)

print("Enumerated for-loop with previous last item now at the front.")
for index, item in enumerate(aList):
    print(index,item)

print("Called the .sort() function and sorted the list.")
aList.sort() # Sort list

print("Print sorted list.")
for index, item in enumerate(aList):
    print(index,item)

