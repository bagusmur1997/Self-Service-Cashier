# Supermarket Self-Service Cashier
This is a Python program made for a supermarket self-service cashier that allows customers to add items to their cart, view the cart, update items, and remove items and other feature. The program also has a checkout function that generates a transaction record in an Excel file.

<img src="/img/Main Menu.png"/>

## Features
The following features are currently implemented in the program:
* `add_item()` : Allows the user to add a product to their cart by specifying its name, quantity, and price. If the product is already in the cart, the quantity is updated accordingly.
* `update_item()` : Allows the user to update the name, quantity, and price of a product already in the cart.
* `delete_item()` : Allows the user to remove a product from the cart.
* `view_cart()` : Shows the user the contents of their cart, including the name, quantity, price, and total price of each product, as well as the grand total of the cart.
* `reset_transaction()` : Allows the user to reset the transaction history and clear the cart.
* `checkout()` : Allows the user to checkout their purchases, updating the transaction history and clearing the cart. Before checkout, the user can review the total amount due and confirm the checkout.
* `display_product_list()` : Displaying the inventory list of products available for purchase. the content displays of the products is 'product name, quantity available'.
* `leave_feedback()` : Allow customers to leave feedback To improve the customer experience, this feedback used to improve the app in future updates.

## Test Cases & Results
### Test case 1: Add Item to Cart
**1.A : View Our Inventoy**

<img src="/img/Test A4.png"/>

**1.B : Add Item contain in inventory list**

<img src="/img/Test A2.png"/>

**1.C : Add Item not contain in inventory list**

<img src="/img/Test A3.png"/>

**1.D : View Cart**

<img src="/img/Test A5.png"/>

### Test case 2: Update Item from Cart
**2.A : Update item contain in cart - change item name**
**2.B : Update item contain in cart - change qty item**
**2.C : Update item contain in cart - change price**


**2.D : Update item not contain in cart**

<img src="/img/Test B4.png"/>


