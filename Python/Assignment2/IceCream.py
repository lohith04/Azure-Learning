Cities = ["Miami", "Orlando", "Tampa"]
Flavours = {"Classics": ["Vanilla", "Chocolate", "Strawberry"], 
            "Trendy Flavours": ["Salted Caramel", "Matcha", "Cookies&Cream"], 
            "Kid-Friendly": ["Rainbow Sherbet", "Bubblegum", "Cotton Candy"], 
            "Seasonal Specials": ["Mango", "Pineapple-Coconut", "Key Lime Pie"]}
FlavoursList = []
for category in Flavours.values():
    for flavour in category:
        FlavoursList.append(flavour)
Toppings = { "Sprinkles": 0.50,
            "Crushed Cookies": 0.50,
            "Chocolate Chips": 0.50,
            "Fresh fruit": 0.75,
            "Whipped cream": 0.75,
            "Caramel/Chocolate drizzle": 0.75,
            "Pop Rocks": 1.00, 
            "Tajín spice": 1.00, 
            "Gummy bears": 1.00
}
BaseIceCreamPrices = {"Single Scoop": 3.00,
                       "Double Scoop": 5.50,
                       "Triple Scoop": 7.50}

Combinations = {
    "Classic Pairings": [
        {"Vanilla": ["Chocolate Chips"], 
         "Chocolate": ["Crushed Cookies"], 
         "Strawberry": ["Whipped cream", "Fresh fruit"]
         }],
    "Trendy & Fun Pairings": [
        {"Matcha": ["Caramel/Chocolate drizzle", "Fresh fruit"], 
         "Salted Caramel": ["Sprinkles", "Caramel/Chocolate drizzle"], 
         "Cookies&Cream": ["Chocolate Chips", "Crushed Cookies"]
         }],
    "Kid-Friendly Combos": [
        {"Rainbow Sherbet": ["Sprinkles", "Gummy bears"], 
         "Bubblegum": ["Whipped cream", "Chocolate Chips"], 
         "Cotton Candy": ["Pop Rocks"]
         }],
    "Florida-Inspired Combos": [
        {"Mango": ["Tajín spice", "Fresh fruit"], 
         "Pineapple-Coconut": ["Sprinkles"], 
         "Key Lime Pie": ["Caramel/Chocolate drizzle", "Whipped cream"]}]
}

#Problem1
for City in Cities:
    Count = len(City)
    print(f"Number of letters in '{City}' is {Count}!")

#Problem2
for FlavourList in FlavoursList:
    Count = float(Count + len(FlavoursList))
Average = Count/len(FlavoursList)
print(f"Average length of IceCream flavour is {Average}.2f!")

#Problem3
print(f"List of flavours before sorting alphabetically is: {FlavoursList}")
FlavoursList.sort()
print(f"List of flavours after sorting alphabetically is: {FlavoursList}")

#Problem4
TotalCost = float(Toppings.get("Chocolate Chips") + Toppings.get("Whipped cream") + Toppings.get("Gummy bears"))
print(f"Total cost of Selected toppings: Chocolate Chips, Whipped Cream, and Gummy Bears is: {TotalCost}")

#Problem5
BasePrices = (BaseIceCreamPrices.values())
print(f"Most expensive option is: {max(BasePrices)} and least expensive option is: {min(BasePrices)}")

#Problem6
IceCreamFlavour = input("Enter an icecream floavour to determine if it belongs to Classics or Trendy Flavors or Kid-Friendly or Seasonal Specials: ")
for category, flavors in Flavours.items():
    if IceCreamFlavour in flavors:
        print(f"Entered IceCream Flavour belongs to {category} Category")
        break
    else: 
      print(f"Invalid input enter Floavours only from the following list: {Flavours.values()}")
      break

#Problem7 
BestCity = input("Enter a city to check if it is in the list of suggested cities for the business: ")
if BestCity in Cities:
    print("Valid city")
else:
    print("Invalid city")

#Problem8
BasePrice = BaseIceCreamPrices["Single Scoop"]
for category, pairings in Combinations.items():
    for pairing in pairings:
        for flavor, toppings in pairing.items():
            toppingprice = 0
            for topping in toppings:
                toppingprice += Toppings[topping]
                totalprice = BasePrice + toppingprice
                print(f"{flavor} + {topping}: ${totalprice}")

#Problem9

