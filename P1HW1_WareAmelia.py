# This program will ask the user for information and compute the information for needed answers

# 4-6-23

# CTI-110 P1HW1 - Travel Expense

# Amelia Ware

# Create appropriate variable and assign them as needed later on
budget = 0
destination = 0
gas = 0
acc_hotel = 0
food = 0
#Ask user to enter their budget and have them enter it
print('Enter budget: ', end='')
budget = int(input())
# Ask user to enter travel destination and have them enter it
print('Enter your travel destination: ', end='')
destination = input()
#Ask user for amount they will spend on gas and have them enter it
print('How much do you think you will spend on gas? ', end='')
gas = int(input())
# Ask user for amount they will spend on accommodation and have them enter it
print('Approximately, how much will you need for accomodation/hotel? ', end='')
acc_hotel = int(input())
#Ask user for amount they will spend on food and have them enter it
print('Last, how much do you need for food? ', end='')
food = int(input())
#Show the user all of the collected data
print('------------Travel Expenses------------')
print('Location: ', destination)
print('Initial Budget: ', budget)
print('')
print('Fuel: ', gas)
print('Accomodation', acc_hotel)
print('Food: ', food)
print('')
#Add all of the expenses up
total = gas + acc_hotel + food
#Calculate the remaining balance by subtracting the total expenses from the initial balance
rem_bal = budget - total
#Show the user their remaining balance
print('Remaining Balance', rem_bal)

#Pseudocode

#Create variables
#Ask the user for their budget and assign that answer to the budget variable
#ask the user for their destination and add that to the destination variable
#ask the user for their expected gas prices and assign that to the gas variable
#ask the user for their accomodation expenses and assign it to the hotel variable
#ask the user how much they will need for food and add that to the food variable
#print all of the collected data
#calculate total expenses
#subtract expenses from budget
#display the remaining budget
