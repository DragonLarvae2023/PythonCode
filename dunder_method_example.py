# __new__ is executed during the time of the object created and if defined it 
class someClass:
  def __new__(self):
    print(self)
  def fn(self):
    print(self)
obj=someClass()

# a class inheriting from the object class and making the use of the new dunder or magic method
class Student(object):
  name="charles keth dashwood"
  age=19
  def __new__(cls):
    return super(Student,cls).__new__(cls)
  def __init__(self):
    print("init has been called and object reference has been passed")
  @classmethod
  def reset(cls):
    print("all the instance of this class have been reset")
    cls.age=20
obj1=Student()
obj1.age=23
print(obj1.age)
Student.reset()
print(obj1.age)