import menu
from menu import MENU, resources






def check_ingredients(user):
    resources_water = resources['water']
    resources_milk = resources['milk']
    resources_coffee = resources['coffee']
    resources_cost = resources['cost']

    def check_money(user, quarters_coin, dimes_coin, nickels_coin, pennys_coin,resources_water,resources_milk,resources_coffee,resources_cost):

        cost = float(MENU[user]["cost"])
        quarters_coin = float(quarters_coin) * 0.25
        dimes_coin = float(dimes_coin) * 0.10
        nickels_coin = float(nickels_coin) * 0.05
        pennys_coin = float(pennys_coin) * 0.01

        result = float(quarters_coin + dimes_coin + nickels_coin + pennys_coin)
        print(result)

        if result > cost:
            ex_change = result - cost
            change = round(ex_change, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {user} ☕️. Enjoy!")

            if user == 'espresso' :
                water = int(MENU[user]["ingredients"]['water'])
                coffee = int(MENU[user]["ingredients"]['coffee'])

                resources_water -= water
                resources_coffee -= coffee
                resources_cost += cost
                print(resources_water,resources_coffee,resources_cost)
                resources['water'] = resources_water
                resources['coffee'] = resources_coffee
                resources['cost'] = resources_cost

            else:
                water = int(MENU[user]["ingredients"]['water'])
                milk = int(MENU[user]["ingredients"]['milk'])
                coffee = int(MENU[user]["ingredients"]['coffee'])
                cost = float(MENU[user]["cost"])

                resources_water -= water
                resources_milk -= milk
                resources_coffee -= coffee
                resources_cost += cost
                print(resources_water,resources_milk,resources_coffee,resources_cost)
                resources['water'] = resources_water
                resources['milk'] = resources_milk
                resources['coffee'] = resources_coffee
                resources['cost'] = resources_cost





        else:
            print("Sorry that's not enough money. Money refunded.")




    if user == 'espresso':
        water = int(MENU[user]["ingredients"]['water'])
        coffee = int(MENU[user]["ingredients"]['coffee'])

        if resources_water < water:
            print("Sorry there is not enough water.")

        elif resources_coffee < coffee:
            print("Sorry there is not enough coffee.")

        else:
            print("Please insert coins.")
            quarters_coin = input("how many quarters?: ")

            dimes_coin = input("how many dimes?: ")

            nickels_coin = input("how many nickles?: ")

            pennys_coin = input("how many pennies?: ")

            check_money(user, quarters_coin, dimes_coin, nickels_coin, pennys_coin,resources_water,resources_milk,resources_coffee,resources_cost)


    elif user == "report":

        resources_water = resources['water']
        resources_milk = resources['milk']
        resources_coffee = resources['coffee']
        resources_cost = int(resources['cost'])


        print(f"Water: {resources_water}ml\nMilk: {resources_milk}ml\nCoffee: {resources_coffee}g\nCost: ${resources['cost']}")


    else:

        water = int(MENU[user]["ingredients"]['water'])
        milk = int(MENU[user]["ingredients"]['milk'])
        coffee = int(MENU[user]["ingredients"]['coffee'])
        cost = int(MENU[user]["cost"])

        if resources_water < water:
            print("Sorry there is not enough water.")

        elif resources_milk < milk:
            print("Sorry there is not enough milk.")

        elif resources_coffee < coffee:
            print("Sorry there is not enough coffee.")

        else:
            print("Please insert coins.")
            quarters_coin = input("how many quarters?: ")

            dimes_coin = input("how many dimes?: ")

            nickels_coin = input("how many nickles?: ")

            pennys_coin = input("how many pennies?: ")

            check_money(user, quarters_coin, dimes_coin, nickels_coin, pennys_coin,resources_water,resources_milk,resources_coffee,resources_cost)




machine = True

while machine:

    user = input("What would you like? (espresso/latte/cappuccino):")


    if user == 'off':
        machine = False

    else:
        check_ingredients(user)

