from art import logo
print(logo)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user1 = input("Do you wanna see report😊? type 'y' or 'n': ")
if user1 == 'y':
    print(resources)


# for key in MENU:
#     print(f"{key}: "+str(MENU[key]['ingredients']['water']) +"g")

def check():
    # TODO 1
    if resources['water'] < MENU[ask1]['ingredients']['water']:
        print("Sorry! there is not enough water!")
        user1 = input("Do you wanna see report😊? type 'y' or 'n': ")
        if user1 == 'y':
            print(resources)
        return False

    elif resources['water'] > MENU[ask1]['ingredients']['water']:
        if resources['coffee'] < MENU[ask1]['ingredients']['coffee']:
            print("Sorry😔! there is not enough coffee!")
            user1 = input("Do you wanna see report😊? type 'y' or 'n': ")
            if user1 == 'y':
                print(resources)
            return False

        elif resources['coffee'] > MENU[ask1]['ingredients']['coffee']:
            if ask1 == "espresso":
                print("Please insert coins to prepare your order😊")
                quarter = int(input("Please enter your quarters : "))
                dimes = int(input("Please enter your dimes: "))
                nickel = int(input("Please enter your nickel: "))
                pennie = int(input("Please enter your pennie: "))
                # TODO3
                total = ((0.25 * quarter) + (0.10 * dimes) + (0.05 * nickel) + (0.01 * pennie))
                if total > MENU[ask1]['cost']:
                    resources['water'] -= MENU[ask1]['ingredients']['water']
                    resources['coffee'] -= MENU[ask1]['ingredients']['coffee']
                    print(f"Here is your change 😊 {total - MENU[ask1]['cost']}")
                    return True
                elif total < MENU[ask1]['cost']:
                    print("Sorry😔! That's is not enough money, Your money is refunded")
                elif total == MENU[ask1]['cost']:
                    resources['water'] -= MENU[ask1]['ingredients']['water']
                    resources['coffee'] -= MENU[ask1]['ingredients']['coffee']
                    print("Here is your espresso sir ☕, please enjoy this,")
                    return True

            elif resources['milk'] < MENU[ask1]['ingredients']['milk']:
                print("Sorry 😔! there is not enough milk!")
                user1 = input("Do you wanna see report😊? type 'y' or 'n': ")
                if user1 == 'y':
                    print(resources)
                return False

            elif resources['milk'] > MENU[ask1]['ingredients']['milk']:
                ask3 = input("Please insert coins to prepare your order😊")
                quarter = int(input("Please enter your quarters : "))
                dimes = int(input("Please enter your dimes: "))
                nickel = int(input("Please enter your nickel: "))
                pennie = int(input("Please enter your pennie: "))

                # TODO3
                total = ((0.25 * quarter) + (0.10 * dimes) + (0.05 * nickel) + (0.01 * pennie))
                if total > MENU[ask1]['cost']:
                    resources['water'] -= MENU[ask1]['ingredients']['water']
                    resources['milk'] -= MENU[ask1]['ingredients']['milk']
                    resources['coffee'] -= MENU[ask1]['ingredients']['coffee']
                    print(f"Here is your change {total - MENU[ask1]['cost']}")
                    print(f"Here is your {ask1} sir ☕, please enjoy this,")

                    return True
                elif total < MENU[ask1]['cost']:
                    print("Sorry 😔! That's is not enough money, Your money is refunded")
                elif total == MENU[ask1]['cost']:
                    resources['water'] -= MENU[ask1]['ingredients']['water']
                    resources['milk'] -= MENU[ask1]['ingredients']['milk']
                    resources['coffee'] -= MENU[ask1]['ingredients']['coffee']
                    return True

ask1 = input("What would you like? (espresso/latte/cappuccino): ")
check()
