"""
A set of examples to demonstrate the use of conditional/selection statements
suggested by
ChatGPT (https://chat.openai.com/), Feb. 14, 2023

Author:
    Amin G. Alhashim
    aalhashi@macalester.edu
"""

# Unary Conditional/Selection
"""
Prompts the user to enter the number of nights they will be staying at a 
hotel. The base rate for one night's stay is
set to $100, and there is a 20% discount rate for stays of 3 or more nights.
"""
# numOfNights = int(input("Enter number of nights: "))
# total = 100*numOfNights
# if numOfNights >= 3:
# 	total = total * .8
#
# print("Total for {} nights is {:.2f}".format(numOfNights, total))

# Binary Conditional/Selection
"""
Prompts the user to enter the total amount of their restaurant bill. The 
program then calculates the recommended tip 
amount based on the bill total.  If the bill total is less than $50, 
the program calculates a 15% tip.  Otherwise,
the program calculates a 20% tip.
"""
# amount = float(input("Enter amount: "))
# tip = 0;
# if amount < 50:
# 	tip = amount * .15
# else:
# 	tip = amount * .2
# print("Recommened tip is {:.2f}".format(tip))

# Nested Conditional/Selection
"""
A program that helps a user select a travel destination based on their 
preferences
"""
# print("Welcome to the travel destination selector!")
# print(
# 	"Please answer the following questions to help us find your ideal "
# 	"destination.")
#
# budget = int(input("What is your budget for this trip (in dollars)? "))
# climate = input("Do you prefer a hot or cold climate? ").lower()
# activity = input("Do you prefer an adventurous or relaxing vacation? ").lower()
#
# if budget >= 500 and budget <= 1000:
# 	if climate == "hot" and activity == "adventurous":
# 		print("Your ideal destination is Costa Rica!")
# 	elif climate == "hot" and activity == "relaxing":
# 		print("Your ideal destination is Hawaii!")
# 	elif climate == "cold" and activity == "adventurous":
# 		print("Your ideal destination is Banff, Canada!")
# 	elif climate == "cold" and activity == "relaxing":
# 		print("Your ideal destination is Iceland!")
# 	else:
# 		print(
# 			"We couldn't find your ideal destination. Please try again with "
# 			"different preferences.")
# else:
# 	print("Sorry, we could not find any destinations within your budget.")
# 	if budget < 500:
# 		print(
# 			"Consider saving more for your trip or looking for destinations "
# 			"closer to home.")
# 	elif budget >= 10000:
# 		print(
# 			"You have a generous budget! Consider exploring more exotic "
# 			"destinations or splurging on a luxury trip.")
# 	elif budget >= 5000:
# 		print(
# 			"You have a decent budget! Consider visiting popular tourist "
# 			"destinations or taking a cruise.")
# 	else:
# 		print(
# 			"You have a moderate budget! Consider visiting nearby cities or "
# 			"exploring off-the-beaten-path destinations.")
#
# # Chained Conditional/Selection
# """
# A program that asks the user to input the current weather condition and then
# suggests appropriate clothing
#
#
# """
# weather = input(
# 	"What is the current weather condition? (sunny/rainy/snowy/other): ")
#
# if weather == "sunny":
# 	print("Wear a hat, sunglasses, and sunscreen.")
# elif weather == "rainy":
# 	print("Bring an umbrella and wear a raincoat.")
# elif weather == "snowy":
# 	print("Wear a warm coat, gloves, and boots.")
# else:
# 	print(
# 		"Sorry, we couldn't find appropriate clothing recommendations for "
# 		"your "
# 		"weather condition.")
