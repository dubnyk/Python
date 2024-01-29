print('Enter places you would like to visit, they will be stored in a file.')
print('Input "quit" to quit.\n')

with open('travel-list.txt', 'a') as file:
  while True:
    country = input("Country: ")
    if country == "quit":
      break
    else:
      file.write(country + "\n")

print('Okay, goodbye!')
