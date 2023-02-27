expenses= [10.50, 8,5,15,20,5,3]
""" sum = 0 

for x in expenses:
    sum = sum+x """
total = sum(expenses)

print("You spent $", total," on lunch this week.", sep = "")

# adding a input

total = 0
expenses = []

for i in range(7):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)
print("You spent $", total, sep= '')