age=int(input("Enter the Age:"))
if age<10:
	print("The Ticket Rate is 7")
elif age>=10 and age<60:
	print("The Ticket Rate is 10")
elif age>=60:
	print("The Ticket Rate is 5")
else:
	print("Invalid Entry")
