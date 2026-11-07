print("Answer the following question")
print()
childsMeal=input("How much is the price of the child's meal? ")
adultsMeal=input("How much is the price of the adult's meal? ")
children=input("How many children are there? ")
adult=input("How many adults are there?")
print()

# What is the price of a child's meal? 
print(f"Child's meal: ${childsMeal}")
# What is the price of an adult's meal?
print(f"Adult's meal: ${adultsMeal}")
# How many children are there?
print(f"Children: {children}")
# How many adults are there? 
print(f"Adults: {adult}")

# Subtotal: $36.00
print(f"Subtotal: ${float(childsMeal) * int(children) + float(adultsMeal) * int(adult)}")

# What is the sales tax rate? 6
print(f"Sales tax rate: 6%")
# Sales Tax: $2.16
print(f"Sales Tax: ${round((float(childsMeal) * int(children) + float(adultsMeal) * int(adult)) * 0.06, 2)}")
# Total: $38.16
print(f"Total: ${round((float(childsMeal) * int(children) + float(adultsMeal) * int(adult)) * 1.06, 2)}")

# What is the payment amount? 40
payment=input("What is the payment amount? ")
# Change: $1.84
print(f"Change: ${round(float(payment) - round((float(childsMeal) * int(children) + float(adultsMeal) * int(adult)) * 1.06, 2), 2)}")
