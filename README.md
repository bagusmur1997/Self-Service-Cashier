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

### `add_item()`
This Function is essential part of the self-service cashier program because it allows customers to add items to their cart, which is crucial for the checkout process. The function ensures that the inventory is properly managed and that customers are not able to purchase more items than are available in the store.
This is the scenario for this code :
1. The function checks whether the item is available in the inventory by iterating over the rows in the product database using the iterrows() method. If the item is found in the inventory, the function checks whether the item is already in the customer's cart.
2. If the item is not in the cart, the function checks whether there is enough inventory to fulfill the customer's order. If there is enough inventory, the item is added to the cart, and the function prints a confirmation message with the item's name, quantity, and price.
3. If the item is already in the cart, the function checks whether the combined quantity of the item in the cart and the requested quantity exceed the available inventory. If there is enough inventory, the function updates the quantity of the item in the cart and prints a confirmation message with the new quantity and price.
4. If there is not enough inventory to fulfill the customer's order, the function prints an error message with the item's name and the available quantity in the inventory.
5. If the item is not found in the inventory, the function prints an error message indicating that the item is not available for purchase.

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
**2.A : Update item contain in cart - change item name only**

<img src="/img/Test B1.png"/>

**2.B : Update item contain in cart - change qty item only**

<img src="/img/Test B2.png"/>

**2.C : Update item contain in cart - change price only**

<img src="/img/Test B3.png"/>

**2.D : Result View Cart after all change (item, qty, price)**

<img src="/img/Test B5.png"/>

**2.E : Update item not contain in cart**

<img src="/img/Test B4.png"/>

### Test case 3: Remove Item from Cart

<img src="/img/Test C1.png"/>

### Test case 4: Reset all transaction

<img src="/img/Test D1.png"/>

### Test case 5: Check Out Transaction

**5.A : View Our Inventoy before check out transaction & List Item to checkout**

<img src="/img/Test E1.png"/>

<img src="/img/Test E2.png"/>

**5.B : Check Out Process and Total Amount Price & Discount Applied**

<img src="/img/Test E3.png"/>

**5.C : View Our Inventoy after check out transaction**

<img src="/img/Test E4.png"/>

**5.D : Recapitulation Transaction Done in Excel File & Feedback in TXT File**

<img src="/img/Test E5.png"/>

<img src="/img/Test E6.png"/>
