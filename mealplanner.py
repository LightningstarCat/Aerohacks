import random
#lists
veggies = ["carrot","potato","lettuce","onion","avocodo","spinach","squash","pumpkin","mushroom","broccoli","celery","corn","garlic","pepper","tomato","zucchini"]
wholegrain = ["barley","black rice","brown rice","red rice","wild rice","oatmeal","whole-wheat flour","whole-wheat bread","whole-wheat pasta","millet","quinoa"]
fruit = ["strawberry","blueberry","pineapple","orange","lemon","cranberry","grape","mango","banana","apple","watermelon","kiwi","dragonfruit"]
protein = ["egg","bean","pea","lentil","nut","seed","soy products","greek yogart","cottage cheese"]
healthyfat = ["chia","flax","hemp","olive","canola","sunflower","oat","buckwheat","soy"]

print("Hello! I am a meal planner that helps arrange balanced and delicious meals. Let's get started!")

veggiemonday = random.choice(veggies)
wgrainmonday = random.choice(wholegrain)
fruitmonday = random.choice(fruit)
proteinmonday = random.choice(protein)
healthyfatmonday = random.choice(healthyfat)
veggietuesday = random.choice(veggies)
wgraintuesday = random.choice(wholegrain)
fruittuesday = random.choice(fruit)
proteintuesday = random.choice(protein)
healthyfattuesday = random.choice(healthyfat)
veggieweds = random.choice(veggies)
wgrainweds = random.choice(wholegrain)
fruitweds = random.choice(fruit)
proteinweds = random.choice(protein)
healthyfatweds = random.choice(healthyfat)
veggiethurs = random.choice(veggies)
wgrainthurs = random.choice(wholegrain)
fruitthurs = random.choice(fruit)
proteinthurs = random.choice(protein)
healthyfatthurs = random.choice(healthyfat)
veggiefri = random.choice(veggies)
wgrainfri = random.choice(wholegrain)
fruitfri = random.choice(fruit)
proteinfri = random.choice(protein)
healthyfatfri = random.choice(healthyfat)
veggiesat = random.choice(veggies)
wgrainsat = random.choice(wholegrain)
fruitsat = random.choice(fruit)
proteinsat = random.choice(protein)
healthyfatsat = random.choice(healthyfat)
veggiesun = random.choice(veggies)
wgrainsun = random.choice(wholegrain)
fruitsun = random.choice(fruit)
proteinsun = random.choice(protein)
healthyfatsun = random.choice(healthyfat)
    

print("On Monday, you should have " + veggiemonday +", "+ wgrainmonday +", "+ fruitmonday +", "+ proteinmonday +", "+ healthyfatmonday + ".")
print("On Tuesday, you should have " + veggietuesday +", "+ wgraintuesday +", "+ fruittuesday +", "+ proteintuesday +", "+ healthyfattuesday + ".") 
print("On Wednesday, you should have " + veggieweds +", "+ wgrainweds +", "+ fruitweds +", "+ proteinweds +", "+ healthyfatweds + ".") 
print("On Thursday, you should have " + veggiethurs +", "+ wgrainthurs +", "+ fruitthurs +", "+ proteinthurs +", "+ healthyfatthurs + ".") 
print("On Friday, you should have " + veggiefri +", "+ wgrainfri +", "+ fruitfri +", "+ proteinfri +", "+ healthyfatfri + ".") 
print("On Saturday, you should have " + veggiesat +", "+ wgrainsat +", "+ fruitsat +", "+ proteinsat +", "+ healthyfatsat + ".") 
print("On Sunday you should have " + veggiesun +", "+ wgrainsun +", "+ fruitsun +", "+ proteinsun +", "+ healthyfatsun + ".")