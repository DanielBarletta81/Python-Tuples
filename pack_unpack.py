#3. Mastering Tuple Packing and Unpacking in Python


#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order.
#  Each tuple contains the customer's name, the product ordered, and the quantity. 
# 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:

#orders = [
 #   ("Alice", "Laptop", 1),
  #  ("Bob", "Camera", 2),
    # More orders...

#- Write a function to iterate over the list of orders.
#  - Unpack each tuple in the list and format the details for display.

customer_orders = [
    ("Daniel", "iPad", 1),
    ("Christie", "notebook", 4),
    ("Cal", "poster", 8),
    ("Ila", "elmo book", 3)
]
order1, order2, order3, order4 = customer_orders

def display_orders():
  
   # customer = customer_orders[0][0]
   
    
    for i, order in enumerate(customer_orders):
        print(f'Order # {i+1}')
        customer = order[0]
        product = order[1]
        quantity = order[2]
        print(f'Customer: {customer}')
        print(f'Product: {product}')
        print(f'Quantity: {quantity}')
        print("-----------------")
   
            
        

display_orders()