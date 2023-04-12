# Supermarket Self-Service Cashier
This is a Python program made for a supermarket self-service cashier that allows customers to add items to their cart, view the cart, update items, and remove items and other feature. The program also has a checkout function that generates a transaction record in an Excel file.

<img src="/img/Main Menu.png"/>

## Features
The following features are currently implemented in the program:
* `display_product_list()` : Displaying the inventory list of products available for purchase. the content displays of the products is 'product name, quantity available'.
* `add_item()` : Allows the user to add a product to their cart by specifying its name, quantity, and price. If the product is already in the cart, the quantity is updated accordingly.
* `update_item()` : Allows the user to update the name, quantity, and price of a product already in the cart.
* `delete_item()` : Allows the user to remove a product from the cart.
* `view_cart()` : Shows the user the contents of their cart, including the name, quantity, price, and total price of each product, as well as the grand total of the cart.
* `reset_transaction()` : Allows the user to reset the transaction history and clear the cart.
* `checkout()` : Allows the user to checkout their purchases, updating the transaction history and clearing the cart. Before checkout, the user can review the total amount due and confirm the checkout.
* `leave_feedback()` : Allow customers to leave feedback To improve the customer experience, this feedback used to improve the app in future updates.

### add_item()
This Function is essential part of the self-service cashier program because it allows customers to add items to their cart, which is crucial for the checkout process. The function ensures that the inventory is properly managed and that customers are not able to purchase more items than are available in the store.
This is the scenario for this code :
1. The function checks whether the item is available in the inventory by iterating over the rows in the product database using the iterrows() method. If the item is found in the inventory, the function checks whether the item is already in the customer's cart.
2. If the item is not in the cart, the function checks whether there is enough inventory to fulfill the customer's order. If there is enough inventory, the item is added to the cart, and the function prints a confirmation message with the item's name, quantity, and price.
3. If the item is already in the cart, the function checks whether the combined quantity of the item in the cart and the requested quantity exceed the available inventory. If there is enough inventory, the function updates the quantity of the item in the cart and prints a confirmation message with the new quantity and price.
4. If there is not enough inventory to fulfill the customer's order, the function prints an error message with the item's name and the available quantity in the inventory.
5. If the item is not found in the inventory, the function prints an error message indicating that the item is not available for purchase.

### update_item()
This Function is essential feature of the self-service cashier program because it allows customers to make adjustments to their order, ensuring that they can purchase the products they need at the correct quantities and prices. By allowing customers to update their order, the program provides a more efficient and satisfying shopping experience. The function takes an item name as an argument and checks if it is already in the cart with this scenario :
1. If the item is in the cart, the function prompts the user to enter the new product name for the item. If the user enters a new name, the function checks if the new name is available in the store's inventory. If the new name is available, the function updates the item's name in the cart.
2. Next, the function prompts the user to enter a new quantity for the item. If the user enters a new quantity, the function checks if there is enough inventory in the store to fulfill the customer's request. If there is enough inventory, the function updates the quantity of the item in the cart.
3. The function also prompts the user to enter a new price for the item. If the user enters a new price, the function updates the item's price in the cart.
4. Finally, the function prints a confirmation message with the updated name, quantity, and price of the item.
5. If the item is not in the cart, the function prints an error message indicating that the item is not available for update and prompts the user to add the item first.

### delete_item()
This method allows the user to remove an item from the shopping cart. It takes one parameter, name_item, which is the name of the item to be removed. If the item is present in the cart, it is removed using the del keyword, and a message is printed to indicate that the item has been removed. If the item is not present in the cart, a message is printed to indicate that the item was not found in the cart.

### view_cart()
This function is used to view the items in the cart and the total cost of those items. If there are no items in the cart, it will display a message saying that the cart is empty. If there are items in the cart, it will display a table showing the name of each item, the quantity of each item, the price per item, and the total price for each item. It will also display the grand total price for all the items in the cart. The output is formatted using the GitHub markdown syntax, and the tabulate library is used to format the table.

### reset_transaction()
This function is used to reset all transactions made by the user. It clears the user's shopping cart and prints a message indicating that all transactions have been reset successfully.

### checkout()
This is a method to process the checkout of items in a shopping cart. It calculates the total price of the items in the cart, applies a discount if applicable based on the total price, and prompts the user to confirm the checkout. If confirmed, it creates a new row in the transaction history with details of the items purchased, updates the inventory by reducing the quantity of items purchased, saves the updated inventory list to an excel file, and clears the cart. The method also calls another method to prompt the user to leave feedback about their shopping experience. If the checkout is canceled, the cart is not cleared.

### display_product_list()
This is a method to display the current list of products available in the store's inventory. It prints a header and a table containing two columns: 'Product Name' and 'Qty Available'. The data is obtained from the 'self.db' attribute, which is assumed to be a Pandas DataFrame. The table is displayed using the 'tabulate' function from the 'tabulate' library, using the 'github' table format.

### leave_feedback()
this function is used for user to provide a rating and comment about their shopping experience. The rating is expected to be an integer between 1 and 5, and the comment can be any text. The feedback is then stored in a file called feedback.txt in the format "Rating: <rating>, Comment: <comment>". Finally, the user is thanked for their feedback.

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
