#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

    # YOUR CODE STARTS HERE, each line must be indented (one tab)
#Student Name: Hannes Meyer-Rahlfs  
#Program Title:  Tip calculator 

bill = float(input("Enter the original amount of the bill: "))

# Step 3: Assign a variable tax to the value of 15% of the bill
tax = bill * 0.15

# Step 4: Assign a variable tip to the value of 20% of the bill
tip = bill * 0.20

# Step 5: Assign a variable total to the sum of the bill, tip, and tax
total = bill + tax + tip

# Step 6: Display the value of the bill
print("original bill amount", bill)

# Step 7: Display the value of the tax
print("tax (15%)", tax)

# Step 8: Display the value of the tip
print("amount of tip", tip)

# Step 9: Display the value of total
print("total price is", total)


    # YOUR CODE ENDS HERE

