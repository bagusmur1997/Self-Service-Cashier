#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

class Transaction:
    def __init__(self):
        self.cart = {}
        self.db = pd.read_excel("C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Product List.xlsx")
        self.transaction = pd.read_excel("C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Transaction.xlsx")
    
#     def display_product_list(self):
        
    def add_item(self, name_item, qty_item, price_item):
        for index, row in self.db.iterrows():
            if row['Product Name'] == name_item:
                if name_item not in self.cart:
                    self.cart[name_item] = {"qty": qty_item, "price": price_item}
                    print(f"Added {qty_item} {name_item}(s) to cart at ${price_item} each.")
                    return
                else:
                    self.cart[name_item]["qty"] += qty_item
                    self.cart[name_item]["price"] = price_item
                    print(f"Increased {name_item} quantity to {self.cart[name_item]['qty']} at ${price_item} each.")
                    return
        print("Sorry, item not found in the inventory.")

    def update_item(self,name_item):          
        if name_item in self.cart:
            new_name_item = input(f"Enter new product name for {name_item} (press Enter to skip): ")
            if new_name_item.strip():
                self.cart[new_name_item] = self.cart.pop(name_item)
                name_item = new_name_item
                
            new_qty_item = int(input(f"Enter new quantity for {name_item} (press Enter to skip): "))
            if new_qty_item.strip():
                qty_item = int(new_qty_item)
                self.cart[name_item]["qty"] = qty_item
                
            new_price_item = float(input(f"Enter new price for {name_item} (press Enter to skip): $"))
            if new_price_item.strip():
                price_item = float(new_price_item)
                self.cart[name_item]["price"] = price_item
                
            print(f"Updated {name_item} to {qty_item} at ${price_item} each.")
            return
        else:
            print(f"Sorry, {name_item} not found in cart. Plase add the item first.")

        
    def delete_item(self, name_item):
        if name_item in self.cart:
            del self.cart[name_item]
            print(f"Removed {name_item} from the cart.")
        else:
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
            # set the display options
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', None)
            # define formatters for each column
            formatters = {'No': '{:^5}'.format,
                          'Name Item': '{:^15}'.format,
                          'Qty Item': '{:^10}'.format,
                          'Price': '{:^10.2f}'.format,
                          'Total Price': '{:^10.2f}'.format}
            # print the dataframe
            print(df.to_string(index=False, justify='center', formatters=formatters))
            print(f"Grand Total Price for your cart is : ${df['Total Price'].sum()}")
#             for name, details in self.cart.items():
#                 print(f"{name_item} ({details['qty']} x ${details['price']:.2f}) = ${details['qty']*details['price']:.2f}")
                
    def checkout(self):
        if not self.cart:
            print("Cart is empty. Please add items to your cart first.")
            return
        
        else:
            total = sum(details['qty']*details['price'] for details in self.cart.values())
            
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
            print(f"Total amount due: ${total:.2f}")
            if discount_rate > 0:
                print(f"Discount applied ({discount_rate*100:.0f}%): -${discount:.2f}")
                print(f"Discounted price: ${discounted_price:.2f}")
            else:
                print("No discount applied.")
            
            confirm = input("Confirm checkout? (Y/N)").lower()
            if confirm == "y":
                df = pd.DataFrame.from_dict(self.cart, orient='index').reset_index()
                df.columns = ['name', 'qty', 'price']
                df['total'] = df['qty'] * df['price']
                df = self.transaction.append(df)
                df.to_excel("C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Transaction.xlsx", sheet_name='transactions', index=False)
                self.cart.clear()
                print("Thank you for shopping with us!")
                self.cart.clear()
                
            else:
                print("Checkout canceled.")
                
    def reset_transaction(self):
        self.cart.clear()
        print("All transactions have been reset successfully.")

def print_menu():
    print("Menu :")
    print("1. Add item")
    print("2. Update item")
    print("3. Remove item")
    print("4. View cart")
    print("5. Checkout")
    print("6. Reset all transactions")
    print("7. Exit")
    
t = Transaction()
print("Welcome to the supermarket self-service cashier!")

while True:
    print("############################################################")
    print_menu()
    choice = input("Enter choice (1-7): ")
    if choice == "1":
        name_item = input("Enter item name: ")
        qty_item = int(input("Enter quantity: "))
        price_item = float(input("Enter price: $"))
        t.add_item(name_item, qty_item, price_item)
    elif choice == "2":
        name_item = input("Enter item name: ")
        t.update_item(name_item)
    elif choice == "3":
        name = input("Enter item name: ")
        t.delete_item(name_item)
    elif choice == "4":
        t.view_cart()
    elif choice == "5":
        t.checkout()
        break
    elif choice == "6":
        t.reset_transaction()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")


# In[14]:


import pandas as pd
class Product():
    product_list = pd.read_excel("C:/Users/bmurdyantoro/OneDrive - Zuellig Pharma Holdings Pte Ltd/Documents/Pacman Cource/Product List.xlsx")
        
    def __init__(self,name,price,bar_code):
        self.name = name
        self.price = price
        self.bar_code = bar_code

    def display_product(self):
        print(self)  

    def display_product_list(self):
        print("Our inventory")

    def check_product_on_inventory(self):
        found = False       
        for index, product in self.product_list.iterrows():  # use iterrows to loop through DataFrame               
            if self.bar_code == product['Product Code']:                
                product_found = {'Product Name': product['Product Name'],'Price': product['Price'],'Product Code': product['Product Code']}
                found = True
                print(product['Product Name']," -  $"+str(product['Price']),'\n' )

        if found == True :            
            return product_found
        else:
            return False
        
    def set_bar_code(self,bar_code):
        self.bar_code = bar_code

    def set_price(self,price):
        self.price = price    


# In[15]:


barcode = int(input("\nPlease enter the barcode of your item: "))
p1 = Product("","",barcode)
search_product = p1.check_product_on_inventory()


# In[2]:


def scan_product():
    barcode = input("\nPlease enter the barcode of your item: ")
    p1 = Product("","",barcode)
    search_product = p1.check_product_on_inventory()
    if(search_product == False):
        print("This product does not exist in our inventory.\n")
        scan_another()
    else:        
        wishlist.append(search_product)
        scan_another()
    
def scan_another():
    scan_another = input("Would you like to scan another product? (Y/N)")
    if(scan_another == 'y' or scan_another == 'Y'):
        scan_product()

def main():
    scan_product()
    c1 = CheckoutRegister(current_date_time,wishlist)
    total_payment = c1.calculate_payment_due()
    change = c1.pay_money(total_payment)
    #print("Change:",change)
    c1.print_receipt(change)
    print("\nThank you for shopping at FedUni!")

    next = input("(N)ext customer, or (Q)uit? ")
    if(next == "n" or next == "N"):
        wishlist[:] = []
        main()     
    else:
        #sys.exit(0)
        exit()

print("\n--------Welcome to FedUni checkout!--------\n")

main()


# In[ ]:


def add_item(self, item_name, qty, price):
    if item_name in self.items:
        self.items[item_name]['qty'] += qty
        self.items[item_name]['price'] = price
    else:
        self.items[item_name] = {'qty': qty, 'price': price}
    self.total_price += qty * price
    
print("")
name_customer = input("") 

while True:
    action = input("1. Add Item /n 2. Remove Item")

