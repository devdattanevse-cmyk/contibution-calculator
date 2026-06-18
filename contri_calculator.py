#inputs needed 
#rent
# food-order
#electricity 
#people sharing room/flat

#output
#total amount to pay 
number_of_people = int(input("number of people sharing flat: "))
rent = int(input("flat rent or hostel rent : "))
food = int(input("enter amount of food ordered: "))
electricity_spent = int(input("enter the total amount of electricity spent: "))
total_bill = rent+food+electricity_spent
contri_per_person = (total_bill)/number_of_people
print("your payable amount is", contri_per_person)


