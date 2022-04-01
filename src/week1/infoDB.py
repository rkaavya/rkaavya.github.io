InfoDb = []
InfoDb.append({  
               "FirstName": "Kaavya",  
               "LastName": "Raamkumar",  
               "DOB": "April 23",  
               "POB": "La Jolla",  
               "Email": "kaavya.r16@gmail.com",  
               "Owns_Cars":["2010 Acura"]  
              })  

InfoDb.append({  
               "FirstName": "Christina",  
               "LastName": "Lee",  
               "DOB": "April 9",  
               "POB": "Edina",  
               "Email": "christinal19656@stu.powayusd.com",  
               "Owns_Cars":["None"]  
              })
# print(InfoDb)


def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"]) 
    print(InfoDb[n]["DOB"])
    print(InfoDb[n]["POB"])
    print(InfoDb[n]["Email"])
    print("\t", "Cars: ", end="")  
    print(", ".join(InfoDb[n]["Owns_Cars"]))  
    print()

# def tester():
#     print("For loop")
#     for_loop()
#     print("While loop")
#     while_loop(0)  
#     print("Recursive loop")
#     recursive_loop(0)  

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return

# def recur_factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * recur_factorial(n-1)

#saumya's contribution
def driver():
  # print_data()
  for_loop()
  while_loop(0)
  recursive_loop(0)







