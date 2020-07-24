import random
# Integers and Floating Point Numbers
# An Integer
pi = 3.14
radius = 7
result = int(pi * radius)
print(result)

name = "jack"
surname = "stephens"
fullname = (name + " " + surname)
print(name.capitalize())
print(surname.upper())
print(fullname)
# these are strings

# 5
question = input("Is basic training difficult? (yes or no) ").lower()
if question == 'yes':
    print("It only gets easier!")
if question == 'no':
    print("Better start something harder then!")

# 6
budget = int(input('Enter your monthly food budget.'))

if budget <= 0 or budget > 1000:
    print('invalid range')
elif budget > 550:
    print('You will eat well this month!')
elif budget < 550:
    print('This is less than the average American food budget.')
else:
    print('This is the average American food budget.')

# 7

num = 0
while num <= 100:
    num += 2
    print(num)

start, end = 0, 100
for num in range(start, end +1):
    if num % 2 == 0:
        print(num, end = " ")


nums = []

for x in range(1, 100):
    n = random.randint(1, 100)
    nums.append(n)
print(nums)















