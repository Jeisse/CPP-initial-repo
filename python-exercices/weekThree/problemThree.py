# Problem 3: You have been asked to create an application for the Student Union shop which sells caps for 5, shirts for 10 and hoodies for 20.
# Your application should allow the user to input the quantity of each item a student wants to buy and then calculate and output the total cost.
# When you have finished the implementation, test your application to ensure that the calculations are correct.

products = {"caps price: ": 5, "shirtP price: ": 10, "hoodie price: ": 20}
chosenProducts = {}

for x in products:
    qtd = input("Please provide the quantity required for " + x)
    qtdKeyed = {x: (int(qtd) * int(products[x]))}
    chosenProducts.update(qtdKeyed)


total = []
for i in chosenProducts:
    total.append(chosenProducts[i])

print("Total cost: " + str(sum(total)))
