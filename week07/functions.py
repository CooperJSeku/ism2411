# Self-Assessment 
# 1. The first bug I would check is the first error shown in the traceback. I would
#    use the traceback and print() statements to find the line causing the problem.
#    Explaining the code out loud can also help me notice a mistake. This shows that
#    I should debug step by step instead of guessing.
# 2. apply_discount(price, tier) takes a price and a customer tier. It checks the tier
#    and subtracts the matching discount: gold gets 15%, silver gets 10%, bronze gets
#    5%, and any other tier gets no discount. It returns the discounted price, so a
#    colleague can use it by passing in the price and tier.
# 3. The AI use built my understanding, because I used chatgpt but only as a guide for when I needed
#    help with a certain exercise.

#Exercise 1
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


#Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        discount_rate = 0.15
    elif tier == "silver":
        discount_rate = 0.10
    elif tier == "bronze":
        discount_rate = 0.05
    else:
        discount_rate = 0

    return price * (1 - discount_rate)


price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")


#Exercise 3 
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


#Exercise 4 
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#Exercise 5
# The three bugs in broken_sales.py were:
# 1. total = sale replaced the running total instead of adding each sale.
#    Fix: total += sale
# 2. The for statement was missing a colon.
#    Fix: for sale in sales:
# 3. The while loop used i <= len(sales), which tries to access one index
#    beyond the end of the list. Fix: i < len(sales).
# I used ChatGPT to help explain these bugs, which I then used the information the AI gave me
# to use thecorrected version below.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


#Exercise 6 
x = 100  # Global variable

def double_it():
    x = 999  # Local variable; it does not change the global x.
    return x * 2

print(x)            # Prints 100, the global variable.
print(double_it())  # Prints 1998, using the local variable inside the function.
print(x)            # Prints 100 again; the global variable has not changed.

# Scope means where a variable can be accessed. The x inside double_it() is local
# to that function, so it is separate from the global x outside the function.