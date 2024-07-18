f=open("test.txt",'r')
f.read()
print(f.read(10))
for line in f:
  print(line)
print("hi this is the code")
f.close()
f=open("test.txt",'a+')
print(f.write("hi this is the end of the line"))