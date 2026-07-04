items_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 700,
    "milk": 500,
    "coffee": 100,
    "profit": 0
}


def display_latte():
    print("""
     ( (
      ) )
   ........
   |      |] 
   |      |  
    `----'   
Here is Your Latte, Enjoy!\n
    """)


def display_cappuccino():
    print("""
     ( (
      ) )
   ........
   |      |] 
   |      |  
    `----'
Here is Your Cappuccino, Enjoy!\n
    """)


def display_espresso():
    print("""
     ( (
      ) )
   ........
   |      |] 
   |      |  
    `----'   
Here is Your Espresso, Enjoy!\n
    """)


def display_report(water, milk, coffee):
    print(f"""
  ___________________________
 |                           |
 |       RESOURCE REPORT      |
 |___________________________|
 | Water:    {water} ml           |
 | Milk:     {milk} ml           |
 | Coffee:   {coffee} g           |
 |___________________________|
 |      Keep your resources   |
 |       in check always!     |
 |___________________________|
    """)


def display_welcome():
    print("""\n
 _____        __  __                            _   _____          
|  __ \\      | _|| _|                          | | |_   _|         
| /  \\/ ___ | |_| |_ ___  ___    __ _ _ __   __| |   | | ___  __ _ 
| |    / _ \\|  _|  _/ _ \\/ _ \\  / _` | '_ \\ / _` |   | |/ _ \\/ _` |
| \\__\\/ (_) | | | ||  __/  __/ | (_| | | | | (_| |   | |  __/ (_| |
 \\____/\\___/|_| |_| \\___|\\___|  \\__,_|_| |_|\\__,_|   \\_/\\___|\\__,_|


""")

