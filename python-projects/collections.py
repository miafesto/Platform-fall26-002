list = [10, 20, 30, 40, 50] # just like an ArrayList in Java
list.append(5)
list.append(6)
list.append(7)
print(list)

list.remove(50)
print(list)

list.pop(4) # removes index place, default = pops the last added element like in a stack
list.pop()
print(list)

list.reverse()
print(list)

list.sort() # sorts in place, not a new list
print(list)

x = list[1:]
print(x)

list.append(20)
list.append(20)
print(list)
count20 = list.count(20)
print(count20)

print(list.index(20)) # prints index of first occurance of 20

copyList = list
copyList[0] = 999
print(copyList)
print(list) # YOU ARE ASSIGNING POINTERS

# if you want to create an actual copy of the list...
copyList = list.copy() # or...
copyList = list[:] 

copyList[-1] = 999
print(copyList, list)

empty = []
print(empty)
for i in list:
    if i >= 20 and i <= 50:
        empty.append(i)
print(empty)

empty[0] * 10 # making a list of size 10
print(empty)

squares = []
for i in range(1, 10):
    squares.append(i * i)
print(squares)

'''
LIST COMPRESSIONS
Making a list by using a for loop within the assignment of the list
You can even add an if statement within it as well
'''
squares = [x * x for x in range(1,10)] # list = [VALUE2STORE, for VAL in range(a, b)]
print(squares)

y = [x for x in list if x <= 50 and x >= 20] # x should be the same var if you want individual elements instead of the whole list
print(y)

aset = (1,2,3,4,3,3,3)
print(aset)
#aset.add(40)
print(aset)

'''
DICTIONARIES
'''
fav_foods = {"kathleen" : "pizza", 'steve' : 'burger', 'mia':'sushi', 'james':'ketchup'}
food = fav_foods['kathleen']
print(food)
if 'bob' in fav_foods:
    print(fav_foods['bob'])
else:
    fav_foods['bob'] = 'ice cream'
print(fav_foods)

for key, value in fav_foods.items():
    print(key,value)