# Created by: Chris Asante
# Created on: April-2019
# Created for: ICS3U
# Assignment 3
# This program calculates the cost of a pizza

subtotal = 0
pizzasize = input(" What choice of size do you want the pizza to be? Input L for large or XL for Extra Large : ")

if pizzasize == "L":
    subtotal+=6
elif pizzasize == "XL":
    subtotal=10
print("The total is $"+str(subtotal))

toppings = input("How many toppings do you want on the pizza? {1 to 4}: ")
toppings = int(toppings)

if toppings == 1:
    subtotal +=1
 
elif toppings == 2:
    subtotal += 1.75
    
elif toppings == 3:
    subtotal += 2.50
    
elif toppings == 4:
    subtotal += 3.25
    
elif toppings > 4:
    print("Not allowed")

print ("You've chose "+str(toppings)+ " toppings")    

sales = subtotal * 0.13
print("Sales tax = $"+str(sales))

totalAmount = subtotal + sales

print ("The subtotal is $" + str(subtotal))
print ("Your total including HST is "+str(totalAmount))