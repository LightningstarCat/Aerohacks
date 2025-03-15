import random
#lists
veggies = ["carrot","potato","lettuce","onion","avocodo","spinach","squash","pumpkin","mushroom","bean","broccoli","celery","corn","garlic","pepper","tomato","zucchini"]
wholegrain = ["barley","black rice","brown rice","red rice","wild rice","oatmeal","whole-wheat flour","whole-wheat bread","","",""]
print("Hello! I am a meal planner that helps arrange healthy and delicious. Let's get started! To start, what food (only one) do you want to avoid?")
avoid = input()
veggiemonday = random.choice(veggie)
graintuesday = random.choice(wholegrain)