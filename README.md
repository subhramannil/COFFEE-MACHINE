# COFFEE-MACHINE
This project is a simple coffee machine simulator built using Python. It allows users to order different types of coffee, check available resources, and manage the inventory of ingredients. The coffee machine can prepare three types of coffee: Espresso, Latte, and Cappuccino, each with its own ingredient requirements and cost.

# Features

## Menu Options: Users can choose from three types of coffee:
Espresso: Requires 50ml of water and 18g of coffee.
Latte: Requires 200ml of water, 150ml of milk, and 24g of coffee.
Cappuccino: Requires 250ml of water, 100ml of milk, and 24g of coffee.
## Resource Management: 
The machine keeps track of available resources (water, milk, and coffee) and informs the user if any ingredient is insufficient to fulfill their order.
## Payment System: 
Users can insert coins to pay for their coffee. The machine calculates the total amount inserted and checks if it meets the cost of the selected coffee. It also provides change if the user overpays.
# User Interaction: 
The program interacts with users through the console, allowing them to view reports of available resources and make selections.

# How to Use
Run the program.
Choose the type of coffee you would like to order by typing espresso, latte, or cappuccino.
If the resources are sufficient, you will be prompted to insert coins.
The machine will process your payment and either dispense your coffee or inform you if there are insufficient funds or resources.

# Code Structure
MENU: A dictionary containing the coffee types, their ingredients, and costs.
resources: A dictionary tracking the available resources in the machine.
check(): A function that checks if the resources are sufficient for the selected coffee and handles the payment process.

# Requirements
Python 3.x

# Future Improvements
Implement a graphical user interface (GUI) for better user experience.
Add functionality to refill resources.
Include a logging system to track sales and inventory changes.
