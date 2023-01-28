# 1. Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

student = ['Matt', 'Ji', 'Cody', 'Colin', 'Krissy']

print(student[1])
print(student[4])

   

# 2. Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ('cake', 'chicken', 'steak', 'pie', 'chips')
for x in foods:
    print(x, "is good food")