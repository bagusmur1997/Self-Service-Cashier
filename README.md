# Supermarket Self-Service Cashier
This is a Python program for a supermarket self-service cashier for Andi's supermarket that allows customers to add items to their cart, view the cart, update items, and remove items and other feature. The program also has a checkout function that generates a transaction record in an Excel file.

## Features
The following features are currently implemented in the program:
* `add_item` : Allows the user to add a product to their cart by specifying its name, quantity, and price. If the product is already in the cart, the quantity is updated accordingly.
* `update_item` : Allows the user to update the name, quantity, and price of a product already in the cart.
* `delete_item` : Allows the user to remove a product from the cart.
* `view_cart` : Shows the user the contents of their cart, including the name, quantity, price, and total price of each product, as well as the grand total of the cart.
* `reset_transaction` : Allows the user to reset the transaction history and clear the cart.
* `checkout` : Allows the user to checkout their purchases, updating the transaction history and clearing the cart. Before checkout, the user can review the total amount due and confirm the checkout.
* `leave_feedback` : Allow customers to leave feedback To improve the customer experience, this feedback used to improve the app in future updates.
