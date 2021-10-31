motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


motorcycles[1] = 'ducati'
print(motorcycles)



# Using the .append method , to add a value to the list, the new value is appended to the end of the list. 
motorcycles.append('yamaha')
print(motorcycles)



#starting with a blank list and inserting individual entries via the insert() method
military_jets = []
military_jets.insert(0, 'F15')
print(military_jets)



#Modifying an existing list with a new entry, adding to a desired location on the list, this ]
#differs from the typical append, which only adds to the end of the list

motorcycles.insert(1, 'mitsubishi')
print(motorcycles)

# deleting a value from a list if you know its current location within the list
print(motorcycles)
del motorcycles[1]
print (motorcycles)



#using the pop function , this enables the removal of a value from a list but then being able to call upon that removed value. 
# think of a destroyed alien craft, the removal of this craft from the list of active crafts , but then using the popped location 
# to draw an explosion with the location of the pop value. 
# pop specifically removes the last value in the list
# Variable is assigned called popped motorcycles

print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)





cars = ['mazda 323', 'toyota levin', 'toyota avensis']
print(cars)

last_owned = cars.pop()
print(f"The last car I owned was a {last_owned.title()}.")
print(cars)


first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned.title()}.")
print(cars)




print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)


# Removing the value denoted as too expensive
# the using the variable too_expensive within a string.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Not removing the value, but using the first value in the list and assigning the variable too_expensive to the list value and printing. 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = motorcycles[0]
print(f"\nA {too_expensive.title()} is too expensive for me.")
print(motorcycles)

motorcycles.remove(too_expensive)
print(motorcycles)