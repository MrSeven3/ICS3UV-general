"""
===============================================
Assignment 1 – Python Programming
Student Name: Grayson Vantilborg
Date: 2026-09-14

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say Hello
# Write a program that asks the user for their name
# and prints: Hello, <name>!
# =======================================================

# --- Put your code here ---

#get name
name = input("What is your name? ")
#output it
print(f"Hello, {name}!")

# =======================================================
# Question 2: Adding Numbers
# Ask the user to enter two numbers. Add them together
# and print the result.
# =======================================================

# --- Put your code here ---

#get numbers
q2_number_1 = float(input("Enter the first number: "))
q2_number_2 = float(input("Enter the second number: "))

#calculate and output
q2_sum = q2_number_1 + q2_number_2
print(f"The sum is {q2_sum}")

# =======================================================
# Question 3: Average of Three Numbers
# Ask the user to enter three numbers. Calculate the
# average and print it.
# =======================================================

# --- Put your code here ---

#get numbers
q3_number_1 = float(input("Enter the first number: "))
q3_number_2 = float(input("Enter the second number: "))
q3_number_3 = float(input("Enter the third number: "))

#calculate and output
q3_avg = (q3_number_1 + q3_number_2 + q3_number_3) / 3
print(f"The average is {q3_avg:.4f}")


# =======================================================
# Question 4: Pizza Shop – Calculate Tax
# Ask the user to enter the total cost of their order.
# Calculate 13% tax and print the total amount including tax.
# ===============

# --- Put your code here ---

#get price
q4_price = float(input("Enter the cost of your order: $"))

#calculate tax and output
q4_tax = q4_price * 0.13
print(f"The tax costs: ${q4_tax:.2f}")

#calculate final cost and output
q4_final_cost = q4_price + q4_tax
print(f"The total cost including tax is ${q4_final_cost:.2f}")

# =======================================================
# Question 5: Rectangle Area Calculator
# Ask the user to enter the length and width of the rectangle
# Calculate the area of the rectangle
# Print the results witha clear message
# RECALL! Area = length * width
# =======================================================

# --- Put your code here ---

#get dimensions
q5_rectangle_length = float(input("Enter the length of the rectangle: "))
q5_rectangle_width = float(input("Enter the width of the rectangle: "))

#calculate and output
q5_rectangle_area = q5_rectangle_length * q5_rectangle_width
print(f"The area of the rectangle is {q5_rectangle_area}")

# =======================================================
# Question 6: Tip Calculator
# Ask the user to enter the total bill amount at a restaurant.
# Ask the user to enter a tip percentage (e.g., 15 for 15%).
# Calculate the tip amount and the total bill including tip.
# Print both values clearly.
# =======================================================

# --- Put your code here ---

#get the numbers
q6_price = float(input("Enter the cost of your bill: $"))
q6_tip_amount = float(input("Enter the tip amount as a percentage: "))

#calculate the extras
q6_tax = q6_price * 0.13
q6_tip = q6_price * (q6_tip_amount / 100)
q6_total = q6_price + q6_tax + q6_tip

#output
print(f"The tax is ${q6_tax:.2f}")
print(f"The tip is ${q6_tip:.2f}")
print(f"The total cost is ${q6_price:.2f}")