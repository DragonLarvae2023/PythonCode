import functools
lis=[1,2,4,10,19,18,21,12,20,22,34]
# demonstration of the map constructor
print(list(map(lambda x:x*2,lis)))
# demonstraton of the reduce constructor
print((functools.reduce(lambda x,y:x*y,lis)))
# demonstration of the filter constructor
print(list(filter(lambda x:x%2==0,lis)))
print(isinstance("hello",str))
# a simple function to check if the elements in a list are starting with a
lis2=[1,2,4,10,19,18,21,12,20,22,34,"apple","orange","banana","angular_fruit"]
def filterElements(lis):
  return list(filter(lambda x:isinstance(x,str)==False or x.startswith("a")==True,lis))
print(filterElements(lis2))
#to get the largest number in the list
import functools

def largestNumber(lis):
    return functools.reduce(lambda x, y: x if not isinstance(y, int) else y if not isinstance(x, int) or x < y else x, lis)

lis3 = ["orange", "mango", "pineapple", 10, 19, 21, 30, 32, 12, 145, 123]
print(largestNumber(lis3))
