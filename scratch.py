# myName = "It's none of your business!"\
# "You should not say that!"

# print(myName[5])
# print(len(myName))

# number1 = 24
# print(float(number1))

# number2 = 2457844555
# print(ord(number2))

# user_num_1 = input('What is the first number is: ')
# user_num_2 = input('What is the second number is: ')
# user_sum = int(user_num_1) + int(user_num_2)
# print(user_sum)

total_bill = 300

bill_discount1 = 30 
bill_discount2 = 10

if total_bill > 100 and total_bill < 200:
    print("The total bill is more than $100") 
    total_bill = total_bill - bill_discount1
elif total_bill > 200:
    total_bill = total_bill - bill_discount2
    print("The total value is greater than $200")
else:
    print("The total bill is less than $100")

print("Total bill is:" + str(total_bill))