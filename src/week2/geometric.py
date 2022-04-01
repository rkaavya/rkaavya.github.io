#saumya's contribution
# defining the geometric sum
# class geometrics:
def geometric_sum(n):
  if n < 0:
    return 0 
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1) #geometric sum formula

# geometric_sum()
# print(geometric_sum(7)) # printing geometric sum for the number 7
# print(geometric_sum(4)) # printing geometric sum for the number 4
# print(geometric_sum(10)) # printing geomeric sum for the number 10

def driver():
  # geometric_sum(7)
  # geometric_sum(4)
  # geometric_sum(10)
  print("Input of 7: " + str(geometric_sum(7)))
  print("Input of 4: " + str(geometric_sum(4)))
  print("Input of 10: " + str(geometric_sum(10)))
  
  
