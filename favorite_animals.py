# survey to get information on people’s favorite animals

# import collections to make count of each unique element easier
from collections import Counter

# user input for survey
animal = []
response = ""
while response.lower() != "x":
    response = input("enter your favorite animal from the survey or 'x' to exit: ").lower().strip()
    if response != "x": animal.append(response)

# determines the final count of the survey and max
print("survey summary:\n" + "-" * 15)
max = 0
count = Counter(animal)
for index, animal in enumerate(count): 
    print(f'{animal}: {count[animal]}')
    if count[animal] > max: max = count[animal]

# determines the most popular animal(s)
print("\npopular animal(s):\n" + "-" * 15) 
popular = []
for index, animal in enumerate(count):
    if count[animal] == max:
        popular.append(f'{animal}: {count[animal]}')
print('\n'.join(map(str, popular)))