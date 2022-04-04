# import other
# from ship import *
# from processing import *
from src.week0 import swap
from src.week0 import ship
from src.week2 import geometric
from src.week2 import *
from src.week1 import infoDB 
# from factorial import *
from src.week1 import fibonacci 
# from src.week2 import bank
from src.week0 import *

main_menu = [
    ["Swap", swap.driver],
    ["Ship Animation", ship.driver],
    ["InfoDB", infoDB.driver],
    ["Geometric Sequences", geometric.driver],  
    ["Keypad/Matrix", "src/week0/keypad.py"],  
]


sub_menu = [
    ["Factorial", "src/week2/factorial.py"],
    ["Bank", "src/week2/bank.py"],
  # ["GCD", None],
    # ["LCM", "geomet.geometric_sum"],
    # ["Primes", None],

]

patterns_sub_menu = [
    # ["Patterns", None],
    # ["PreFuncy", None],
    ["Fibonacci", fibonacci.driver],
    ["Caesar Cipher", "src/week2/caesarcipher.py"]
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
  
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    for key, value in prompts.items():
        print(key, '->', value[0])

    choice = input("Type your choice> ")

  
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")


    buildMenu(banner, options)

if __name__ == "__main__":
    menu()









