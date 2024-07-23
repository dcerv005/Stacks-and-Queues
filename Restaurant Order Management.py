import time

kitchen_orders=[]
customer_orders=[]
#Task 1
def push (kitchen_orders, order):
    kitchen_orders.append(order)
    print(kitchen_orders)
    

#Task 2    
def pop():
    if kitchen_orders:
        
        return kitchen_orders.pop(0)
    else:
        print("There aren't any orders for the kitchen")
    

push(kitchen_orders, "Fries")    

print(f"Next order up: {pop()}")

#Task 3

def enqueue (item):
    customer_orders.append(item)
    print(f"Order: {item}, was added to the queue")
    print(customer_orders)
#Task 4  
def dequeue ():
    if customer_orders:
        return print(f"Order: {customer_orders.pop(0)} is ready for pickup")

order1_start=time.time()        
enqueue("Sandwich")
dequeue()
order1_end=time.time()

print(f"Order took {order1_end-order1_start} seconds to process")
