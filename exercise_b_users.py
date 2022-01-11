users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users['Jonathan']['twitter'])

# 2. Get Erik's hometown
print(users['Erik']['home_town'])

# 3. Get the list of Erik's lottery numbers
eriks_numbers = users['Erik']['lottery_numbers']
print(eriks_numbers)

# 4. Get the species of Avril's pet Monty
avrils_pets = (users['Avril']['pets'])
print(avrils_pets[0]['species'])

# 5. Get the smallest of Erik's lottery numbers
smallest = eriks_numbers[0]
for number in eriks_numbers:
  if number < smallest:
    smallest = number
print(smallest)

# 6. Return an list of Avril's lottery numbers that are even
avrils_numbers = users['Avril']['lottery_numbers']
avrils_even_numbers = []
for number in avrils_numbers:
  if number % 2 == 0:
    avrils_even_numbers.append(number)
print(avrils_even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
eriks_numbers.append(7)
print(eriks_numbers)

# 8. Change Erik's hometown to Edinburgh
users['Erik']['home_town'] = 'Edinburgh'
print(users['Erik']['home_town'])

# 9. Add a pet dog to Erik called "fluffy"
users['Erik']['pets'].append({'name':'fluffy', 'species': 'dog'})
print(users['Erik']['pets'])

# 10. Add another person to the users dictionary
users.update({  "Monika": {
    "twitter": "monia",
    "lottery_numbers": [7, 12, 34, 33, 16, 25],
    "home_town": "Katowice",
    "pets": [
    {
      "name": "hoppy",
      "species": "cat"
    },
    {
      "name": "sweetie",
      "species": "cat"
    }
  ]
  },})
print(users)

