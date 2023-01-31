# 1. Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

student = ['Matt', 'Ji', 'Cody', 'Colin', 'Krissy']

print(student[1])
print(student[4])

   

# 2. Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ('cake', 'chicken', 'ahi tuna', 'pie', 'chips')
for x in foods:
    print(x, "is good food")

# 3. Using a for loop, print just the last two food strings from foods.

for i in range(-2,0):
    print(foods[i])

# 4. Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

hometown = {'city':'Las Vegas','state':'Nevada','population':646790}
print(f"I was born in {hometown['city']}, {hometown['state']} - population of {hometown['population']}")

# 5. Iterate over the key: value pairs in home_town and print a string for each item, for example:
#	"city = Arcadia"
#	"state = California"
#	"population = 58000"

for key, val in hometown.items():
	print( f"{key} = {val}" )

# 6. Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
cohort = []
for idx, students in enumerate(student):
    cohort.append({
        'student': students,
        'fav_food': foods[idx]
    })
    print(cohort[idx])

