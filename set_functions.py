setX={"apple","orange","guava","pineapple",True,23,14}
#iterating over a set
for i in setX:
  print(i)
#checking if one element exist in a set
print("apple" in setX)
#adding an element in a set
print(setX.add("banana"))
print(setX)
#you want to add a set in another set
setY={"orange","grapes"}
setX.update(setY)
print(setX)
#operations on set using operators
print(setX-setY)
print(setX|setY)
print(setX&setY)

# pop functionality
print(setX.pop())

