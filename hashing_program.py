class user:
  def __init__(self,name,password):
    self.name=name
    self.password=password
  def __eq__(self,user2):
    if isinstance(user2,user):
      return self.name==user2.name and self.password==user2.password 
    return False
  def __hash__(self) :
    return hash((self.name,self.password))
user1=user("john jacob",9080)
print(hash(user1))
print(hash(user1)==hash(user1))