# def swap0(age1, age2):
#   c = int(input('Whats your first number?:'))
#   d = int(input('Whats your second number?:'))
#   c,d = swap1(c,d)
#   return(c,d)
  
# def swap0(a,b):
#   if a > b:
#     b, a = a, b  
#   else:
#     a, b = a, b
#   return a, b
#saumya's contribution
def swap1(age1,age2):
  temp = age1
  age1 = age2
  age2 = temp
  print("Swap 1 Result:")
  return age1,age2
  
#returns numbers lowest to highest  
def swap2(a, b):
  if a > b:
    b, a = a, b
  print("Swap 2 Result:")
  return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
  if age1 > age2:
    print ("Swap 3 Result:")
    return(age2, age1)
  else:
    print ("Swap 3 Result:")
    return(age1, age2)

def driver():    
# tests
  print(48, 53)
  print(914, 290)
  print(swap1(48, 53))
  print(swap1(914, 290))
  print(swap2(53, 48))
  print(swap2(290, 914))
  print(swap3(48, 53))
  print(swap3(914, 290))
  
