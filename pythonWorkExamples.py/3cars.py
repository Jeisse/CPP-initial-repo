cars = ['toyota', 'honda','Mitsubishi', 'nissan', 'mazda']
print(cars)

# the above shows ['toyota', 'honda', 'Mitsubishi', 'nissan']
# this is not the output we wish are users to see
# Below we will access individual entries in a list by providing the index of the item

# Accessing Elements in a list 
# Index 0 given , toyota , .title is given to format
print(cars[0].title())


print(cars[3].title())
print(cars[1].title())



print(cars[-1])



print(cars[-2])




print(cars[-3].upper())
print(cars[-3].lower())
print(cars[-3].title())


#Integrating a list value into a string and printing the message with the list value showing. 

message = f"My First Car was a {cars[-1].title()}."
print(message)

message = f'I would like to own a {cars[1].title()}'
print(message)