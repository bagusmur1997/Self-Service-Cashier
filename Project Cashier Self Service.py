import pandas as pd
import datetime
import uuid
from tabulate import tabulate

PRODUCT_LIST = "C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Product List.xlsx"
HISTORY_TRANSACTION = "C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Transaction.xlsx"

class Transaction:
    def __init__(self):
        # creates an empty dictionary to store items added to the cart
        self.cart = {} 
        # reads the product list from an Excel file and stores it in a Pandas DataFrame
        self.db = pd.read_excel(PRODUCT_LIST)
        # reads the transaction history from an Excel file and stores it in a Pandas DataFrame
        self.transaction = pd.read_excel(HISTORY_TRANSACTION)

        try:
            last_id = self.transaction["Transaction ID"].iloc[-1]
            self.last_transaction_id = last_id
        except:
            self.transaction = pd.DataFrame()
            self.last_transaction_id = ""
    
    def get_valid_input(self,prompt,type_func):
        # This while loop prompts the user to enter the quantity/price of an item until a valid integer is entered.
        # The try-except block checks if the input can be converted to an integer, and if not, it gives a warning message and prompts the user to enter a valid integer.     
        while True:
            try:
                user_input = type_func(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def generate_transaction_id(self):
        # generate new transaction id
        while True:
            new_id = str(uuid.uuid4())[:10]
            if new_id != self.last_transaction_id and new_id not in self.transaction["Transaction ID"].tolist():
                self.last_transaction_id = new_id
                return new_id
            
    def print_greeting(self):
        # generate new transaction id
        self.id_transaction = self.generate_transaction_id()
        
        # get current time and date
        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        date = now.strftime("%B %d, %Y")

        # define the store location
        store_location = "Jakarta, Indonesia"

        # define the length of the greeting text
        greeting_text = "Welcome to our self-service cashier!"
        greeting_length = len(greeting_text)

        # print welcome message with proportional # symbols
        print("#" * (greeting_length + 8))
        print("#  {}  #".format(greeting_text.center(greeting_length + 2)))
        print("#" * (greeting_length + 8))
        print("Today's date is {} and the time is {}.".format(date, time))
        print("You are shopping at our store located in {}.".format(store_location))

        # print greeting message with transaction id
        print("This transaction id is {}.".format(self.id_transaction))
        print("#" * (greeting_length + 8))
        
    def start_transaction(self):
        self.print_greeting()
        # start the menu
        while True:
            self.print_menu()
            choice = input("Enter choice (1-8): ")
            if choice == "1":
                name_item = input("Enter item name: ")
                qty_item = self.get_valid_input("Enter quantity: ", int)
                price_item = self.get_valid_input("Enter price: Rp ", float)
                self.add_item(name_item, qty_item, price_item)
                
            elif choice == "2":
                name_item = input("Enter item name: ")
                self.update_item(name_item)
            elif choice == "3":
                name = input("Enter item name: ")
                self.delete_item(name_item)
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.checkout()
                break
            elif choice == "6":
                self.reset_transaction()
            elif choice == "7":
                self.display_product_list()
            elif choice =="8":
                #Exit Program
                print("Thank you for shopping with us today! We hope to see you again soon.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")
            print("############################################")

    def display_product_list(self):
        # This function displays the list of available products in the store inventory.
        print("############################################")
        print("--------------------------------------------")
        print("------Our Store Inventory List Product------")
        print("--------------------------------------------")
        print(tabulate(self.db, showindex=False, headers=['Product Name', 'Qty Available'], tablefmt="github"))
        print("--------------------------------------------")      
    
    def add_item(self, name_item, qty_item, price_item):
        """
        Add an item to the cart with the specified quantity and price, if it exists in the inventory.
        If the item is already in the cart, update its quantity and price.
        Print error messages if the item does not exist or if the inventory does not have enough quantity.
        """
        # iterate over the rows of the product list DataFrame
        for index, row in self.db.iterrows():
            # check if the current row matches the specified item name
            if row['Product Name'] == name_item:
                # if the item is not in the cart yet, add it with the specified quantity and price
                if name_item not in self.cart:
                    if row['Quantity'] >= qty_item:
                        self.cart[name_item] = {"qty": qty_item, "price": price_item}
                        print(f"Added {qty_item} {name_item}(s) to cart at Rp {price_item} each.")
                        return
                    else:
                        print(f"ERROR: Not enough inventory of {name_item} to fulfill order.")
                        print(f"Available quantity of {name_item} is {row['Quantity']}.")
                        return
                # if the item is already in the cart, update its quantity and price
                else:
                    new_qty = self.cart[name_item]["qty"] + qty_item
                    if row['Quantity'] >= new_qty:
                        self.cart[name_item]["qty"] += qty_item
                        self.cart[name_item]["price"] = price_item
                        print(f"Increased {name_item} quantity to {self.cart[name_item]['qty']} at Rp {price_item} each.")
                        return
                    else:
                        print(f"ERROR: Not enough inventory of {name_item} to fulfill order.")
                        print(f"The Available quantity of {name_item} is {row['Quantity']}.")
                        return
        # if the specified item name is not found in the inventory, print an error message
        print("Sorry, item not found in the inventory.")

    def update_item(self,name_item):          
        if name_item in self.cart:
            new_name_item = input(f"Enter new product name for {name_item} (press Enter to skip): ")
            if new_name_item.strip():
                if (new_name_item in self.db['Product Name'].values):
                    self.cart[new_name_item] = self.cart.pop(name_item)
                    name_item = new_name_item
                else:
                    print("Sorry, new item name not found in our inventory.")
                    return
            else:
                new_name_item = name_item
                
            new_qty_item = input(f"Enter new quantity for {name_item} (press Enter to skip): ")
            if new_qty_item.strip():
                available_qty = self.db.loc[self.db['Product Name']==new_name_item,'Quantity'].values[0]
                if available_qty >= int(new_qty_item):
                    qty_item = int(new_qty_item)
                    self.cart[name_item]["qty"] = qty_item
                else:
                    print(f"ERROR: Not enough inventory of {new_name_item} to fulfill order.")
                    print(f"The Available quantity of {new_name_item} is {available_qty}.")
                    return
            else:
                qty_item = self.cart[name_item]["qty"]

            new_price_item = input(f"Enter new price for {name_item} (press Enter to skip): Rp ")
            if new_price_item.strip():
                price_item = float(new_price_item)
                self.cart[name_item]["price"] = price_item
            else:
                price_item = self.cart[name_item]["price"]
            print(f"Updated {name_item} with {qty_item} pcs at Rp {price_item} each.")
            return
        else:
            print(f"Sorry, {name_item} not found in cart. Plase add the item first.")

        
    def delete_item(self, name_item):
        # Check if the item is in the cart
        if name_item in self.cart:
            # If the item is in the cart, delete it from the dictionary
            del self.cart[name_item]
            # Print a confirmation message to the user
            print(f"Removed {name_item} from the cart.")
        else:
            # If the item is not in the cart, print an error message
            print(f"Sorry {name_item} not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart contents:")
            df = pd.DataFrame.from_dict(self.cart, orient='index').reset_index()
            df.columns = ['Name Item', 'Qty Item', 'Price']
            df['Total Price'] = df['Qty Item'] * df['Price']
            df['No'] = df.index + 1
            df = df[['No', 'Name Item', 'Qty Item', 'Price', 'Total Price']]
            print(tabulate(df, showindex=False, headers=['No', 'Name Item', 'Qty Item', 'Price', 'Total Price'], tablefmt="github"))
            print("\n")
            print(f"Grand Total Price for your cart is : Rp {df['Total Price'].sum()}")
                
    def checkout(self):
        if not self.cart:
            print("Cart is empty. Please add items to your cart first.")
            return
        else:
            total = sum(details['qty']*details['price'] for details in self.cart.values())
            discount_rate = 0.0
            # Discount criteria
            if total >= 500_000:
                discount_rate = 0.1
            elif total >= 300_000:
                discount_rate = 0.08
            elif total >= 200_000:
                discount_rate = 0.05
            
            # Calculate the discounted price and the amount of discount
            discount = discount_rate * total
            discounted_price = total - discount
            
           # Print the discounted price and the amount of discount given
            print("--------------------------------------------")  
            self.view_cart()
            print("--------------------------------------------")
            print(f"Total amount due: Rp {total:.2f}")
            if discount_rate > 0:
                print(f"Discount applied ({discount_rate*100:.0f}%): -Rp {discount:.2f}")
                print(f"Discounted price: Rp {discounted_price:.2f}")
            else:
                print("No discount applied.")
            print("--------------------------------------------")  
            
            
            confirm = input("Confirm checkout? (Y/N)").lower()
            if confirm == "y":
                df = pd.DataFrame.from_dict(self.cart, orient='index').reset_index()
                df.columns = ['Product Name', 'Qty', 'Price']
                df['Date Time'] = datetime.datetime.now()
                df['Transaction ID'] = self.id_transaction
                df['Total'] = df['Qty'] * df['Price']
                
                # iterate through the items in the cart and update the inventory list
                for i, item in df.iterrows():
                    # get the product name and quantity from the cart
                    product_name = item['Product Name']
                    qty = item['Qty']
                    # update the inventory quantity
                    self.db.loc[self.db['Product Name'] == product_name, 'Quantity'] -= qty
                # save the updated inventory list to the excel file
                self.db.to_excel(PRODUCT_LIST, index=False)

                df = self.transaction.append(df)
                df.to_excel(HISTORY_TRANSACTION, sheet_name='transactions', index=False)
                self.cart.clear()
                self.leave_feedback()
                print("Thank you for shopping with us!")
                self.cart.clear()
                
            else:
                print("Checkout canceled.")


    
    def leave_feedback(self):
        rating = int(input("Please rate your shopping experience from 1 to 5: "))
        comment = input("Please leave a comment about your experience: ")
        # Store the feedback in a database or file for future analysis
        with open('feedback.txt', 'a') as f:
            f.write(f"Rating: {rating}, Comment: {comment}\n")
        print("Thank you for your feedback!")

    
    def reset_transaction(self):
        self.cart.clear()
        print("All transactions have been reset successfully.")

    def print_menu(self):
        print("Menu :")
        print("{:<2} {}".format("1.", "Add item"))
        print("{:<2} {}".format("2.", "Update item"))
        print("{:<2} {}".format("3.", "Remove item"))
        print("{:<2} {}".format("4.", "View cart"))
        print("{:<2} {}".format("5.", "Checkout"))
        print("{:<2} {}".format("6.", "Reset all transactions"))
        print("{:<2} {}".format("7.", "View store list item"))
        print("{:<2} {}".format("8.", "Exit"))
        print("############################################")
    
t = Transaction()
t.start_transaction()
