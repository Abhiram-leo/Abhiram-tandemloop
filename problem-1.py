class calculator:
  def __init__(self,a:float ,b:float ,operation:str):
    self.a=a
    self.b=b 
    self.operation = operation.lower()
    
  def operations(self)-> float:
    if self.operation == 'addition':
      return self.a + self.b
    elif self.operation =='subtraction':
      return self.a -  self.b
    elif self.operation == 'multiplication':
      return self.a * self.b
    elif self.operation == 'devision':
      if self.b!=0:
        return self.a / self.b
      else:
        raise ValueError("division by 0 error")
    else:
      raise ValueError ("invalid operation    ")
    
    
a=float(input("Enter the number  a"))
b=float(input("Enter the number  b"))
operator=input("Enter the typen of  operation")
calculation=calculator(a,b,operator)
result=calculation.operations()

print(f"result of{a} and {b} is:{result}")


    
