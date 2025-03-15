def dailyactivity():
    print("Ｄａｉｌｙ Ａｃｔｉｖｉｔｙ Ｍａｎａｇｅｒ")
    print("What's your name?")
    name = input()
    print("Hey, I'm Daychat. I'm kind of like an activity log, but I talk! I help you get rid of stress and stimulate your mind. Let's get started. What time did you wake up today?")
    input()
    print("Oh, okay. What did you have for breakfast, " + name + "?")
    input()
    print("Interesting. What's the first thing you do today?")
    input()
    print("Ooh. Any other activities today? You can tell me what you do there too if you like.")
    input()
    print("I kind of wish I could be there instead of stuck in this device! What's for lunch today?")
    input()
    print("Yummmmmm! Are you doing anything after this," + name + "?")
    input()
    print("Okay! What are you having for dinner?")
    input()
    print("Now I really wish I was out of this place. That sounds so delicious! WHat was your favorite part of your meals?")
    input()
    print("Cool. Let's do a reflection! What was your favorite part of the day, " + name + "?")
    input()
    print("I definitely agree with you! What about your least favorite?")
    input()
    print("That's my least favorite part too. Anything cool or unexpected happen? Feel free to go into detail!")
    input()
    print("Ahh. I SOOO want to be there right now! Anyways, that's the end. Have a good night/day!")

def dailyhabit():
    print("ᕼᗩᗷIT TᖇᗩᑕKEᖇ")
    print("Hello! How are you doing?")
    feelpast = input()
    #make habit
    print("I hope you are feeling well! I'm your new habit tracker! I help you make a checklist what you want to do to do a habit daily and stop a bad habit! \n First, let's make a habit! What activity would you like to make a habit? Only one please.")
    habit = input()
    print("Ok! How frequently do you want to do " , habit , "? Put the number of times a day you want to do it.")
    time = input()
    print("Do you think you are doing well on your " , habit , "? Bad, good, great, or awesome?")
    well = input()
    print("Why do you feel that you are doing " , well , " on " , habit , "?")
    whywell = input()
    print("What do you think you need to do to complete " , habit , "?")
    plan = input()
    #bad habit
    print("Next, let's make a plan to stop a bad habit! \n What bad habit would you like to stop?")
    badhabit = input()
    print("Why do you want to stop " , badhabit , "?")
    badreason = input()
    print("What do you think would stop " , badhabit , "?")
    badplan = input()
    print("Ok! Thank you for filling this out! Now I will tell you your plan!")
    print("A new habit you want to make is " , habit , " and to complete that you will" , plan , "" , time , " times a day. For your bad habit, you want to stop " , badhabit , " because " , badreason , ". You will stop this by " , badplan , ".")

def weeklymeal():
    print("░W░e░e░k░l░y░ ░M░e░a░l░ ░P░l░a░n░n░e░r░")
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

def stressmanager():
    print("🆂🆃🆁🅴🆂🆂 🅼🅰🅽🅰🅶🅴🆁")
    print("Hello! I'm The Stress Identifier Algorithm, and I'm here to help you. Let's start with what things make you stressed. Please type the number of the things that make you stressed down below.")
    print("1.) School")
    print("2.) Guilt")
    print("3.) Coworker, friend, or family member")
    print("4.) Your actions")
    print("5.) Life")
    print("6.) Divorce")
    print("7.) Moving")
    print("8.) Injury/Illness/Special Condition")
    print("9.) Financial issues")
    print("10.) Job loss")
    stressq = input()
    if "10" in stressq:
        print("Job loss is hard in the beginning but when you get used to it it isn't so bad. Besides, you can also get another job or just be happy and job free. But if this is keeping you awake at night and cry yourself to sleep, here's what you can do: \n Let your emotions out or at least acknowledge them \n Maintain a routine \n Take some time to focus on yourself \n Spend all your time job searching (not recommended)")
    elif "2" in stressq:
        print("I'm sorry to hear that! Guilt isn't a very good thing to hold. Try telling a trusted friend or guardian about this and see if they can help. WHen you hold guilt for too long, it can have bad outcomes like developing depression, suicidal thoughts, and more! Best get out your guilt quick!")
    elif "3" in stressq:
        print("What a bummer. Friends should be reliable, trustworthy and shouldn't pressure you. This is a hallmark of a bad friend, so you should either warn/tell them that you don't like this. If it's a coworker bothering you, ignore their comments and focus on yourself. If it's a family member, they are probably trying to look out for you or trying to protect you, so talk to them and explain how their chiding is making you feel stressed.")
    elif "4" in stressq:
        print("Your actions shouldn't make you feel stressed! Try righting what you did and move on with your life.")
    elif "5" in stressq:
        print("Life can have its ups and downs. It's important you always keep your purpose in life with you so you can never get stressed about bad things happening to you like this.")
    elif "6" in stressq:
        print("Divorce is a messy and long process that can leave dents in family relationships forever. Parents getting divorced is a big thing happening to you right now, and it can be hard not to break down and hate life. But if you accept it and move on, dealing with divorce might not be so tough once you think about it!")
    elif "7" in stressq:
        print("Moving can be hard once reality actually sinks in. You start worrying that everything won't be fine, your friends and family will forget you. But it's important to remember that you're also doing this for the better, and that no matter what, moving won't change your relationship with friends and family. There will always be a way you can reach them and tell them what's going on.")
    elif "8" in stressq:
        print("When you have one of these, it's important to ask for help if you need it. Writing in a journal can help you let it all out too. Try going out sometimes to stimulate your mind as well!")
    elif "9" in stressq:
        print("Financial issue will always be a problem, but there are ways you can try and stop it. Try making a budget minimize expenses, reduce unneccesary spending, or if it gets too out of hand, talk to someone or ask for help.")
    elif "1" in stressq:
        print("That's sad to hear. School can make people stressed due to testing, homework overload and even peer pressure! If your problem is any of these listed, you can: \n Work on your time management \n Talk to a therapist/counselor \n Or work harder!")

    print("Stress shouldn't be a thing that people stay on and feed off of, so I hope these ideas help or at least get you started and back in life!")

def mainmenu():
    print("𝓜𝓮𝓷𝓾")
    print("Type the number of what you want to do:")
    print("1: Stress Manager")
    print("2: Daily Habit Helper")
    print("3: Daily Activity Log")
    print("4: Balanced Weekly Meal Generator")
    print("5: Relaxation Tactics")
    whatyouwanttodo = input()
    if whatyouwanttodo == "1":
        stressmanager()
    elif whatyouwanttodo == "2":
        dailyhabit()
    elif whatyouwanttodo == "3":
        dailyactivity()
    elif whatyouwanttodo == "4":
        weeklymeal()
    elif whatyouwanttodo == "5":
        relax()
    else:
        print("That's not a valid input...but do you know what is?????")
        print("LOFI!!!!")
        print("Copy and paste into a new tab for the lofi playlist: \n https://open.spotify.com/playlist/5blAlCXRxFevowEHChd2gb")
        print("Copy and paste into a new tab for the positive music: \n https://open.spotify.com/playlist/6CXcW9CVtlhqkCpTfPhy0D")

print("𝔸𝕖𝕣𝕠𝕙𝕒𝕔𝕜𝕤 𝕊𝕖𝕝𝕗-ℍ𝕖𝕝𝕡 ℍ𝕦𝕓")
print("Welcome to Aerohacks Self-Help Hub! We've got many things to help you improve your daily life and overall experence day-to-day.")
while True:
    mainmenu()