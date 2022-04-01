#saumya's contribution
def fibonacci():
    count = int(input("Enter fibonacci sequence count: "))
    n = 0
    while n <= count:
      print(fibonacci1(n),end = " ")
      n+=1
    print()
    return 
  
def fibonacci1(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

def driver():
  fibonacci()
