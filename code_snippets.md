 
{% include navigation.html %}


**_Code Snippets From Challenges_**

**Lists/Loops**

```
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


```

  
  
  
  
**Fibonacci**

```
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

 ```

  
  
  

**Menu**
  
```
 main_menu = [
    ["Swap", swap.driver],
    ["Ship Animation", ship.driver],
    ["InfoDB", infoDB.driver],
    ["Geometric Sequences", geometric.driver],  
    ["Keypad/Matrix", "src/week0/keypad.py"],  
]


sub_menu = [
    ["Factorial", "src/week2/factorial.py"],
    # ["GCD", None],
    # ["LCM", "geomet.geometric_sum"],
    # ["Primes", None],

]

patterns_sub_menu = [
    # ["Patterns", None],
    # ["PreFuncy", None],
    ["Fibonacci", fibonacci.driver],
]

 ```
  
 **One Animation (Ship):**
  ```
 #saumya's contribution

import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
    
def ocean_print():
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)
  

def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    |\   ")
    print(sp + "    |/   ")
    print(SHIP_COLOR, end="")
    print(sp + "\__ |__/ ")
    print(sp + " \____/  ")
    print(RESET_COLOR)
  
def ship():
    ocean_print()
    start = 0  
    distance = 60  
    step = 2  
  
    for position in range(start, distance, step):
      ship_print(position)
      time.sleep(.1)

if __name__ == "__main__":
    ship()

def driver():
  ocean_print()
  pos=12
  ship_print(12)
  ship()




  ```
  
  
