
import random,sys
def print_intro():
    '''Prints the introduction message'''
    print'''Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:
(a) Each person needs at least 20 bushels of grain per year to survive.
(b) Each person can farm at most 10 acres of land.
(c) It takes 2 bushels of grain to farm an acre of land.
(d) The market price for land fluctuates yearly.
Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!'''


def ask_to_buy_land(bushels, cost):
    '''Ask user how many bushels to spend buying land.'''
    acres = input("How many acres will you buy? ")
    while acres * cost > bushels:
        print "O great Hammurabi, we have but", bushels, "bushels of grain!"
        acres = input("How many acres will you buy? ")
    return acres

def ask_to_sell_land(acres):
    '''Ask user how much land they want to sell.'''
    acres_sold = input("How many acres will you sell? ")
    while acres_sold > acres:
        print "O great Hammurabi, we have but", acres, "acres!"
        acres_sold = input("How many acres will you sell? ")
    return acres_sold

def ask_to_feed(bushels):
    '''Ask user how many bushels they want to use for feeding.'''
    feeding = input("How many bushels will you use for feeding?")
    while feeding > bushels:
        print "O great Hammurabi, we have but", bushels, "bushels in storage!"
        feeding = input("How many bushels will you use for feeding?")
    return feeding


def ask_to_cultivate(acres, population, bushels):
    '''Ask user how much land they want to plant seed in'''
    planting_land = input("How much land do you want to plant seed in?")
    while planting_land > acres :
        print "O great Hammurabi, we have but", acres, "acres!"
        planting_land= input("How much land do you want to plant seed in?")
    while planting_land>population*10:
        print "O great Hammurabi, we have but",population,"people to only farm",population*10,"acres"
        planting_land= input("How much land do you want to plant seed in?")
    while planting_land*2>bushels:
        print "O great Hammurabi, we have but",bushels,"bushels to cultivate",bushels/2, "acres!"
        planting_land= input("How much land do you want to plant seed in?")
    return planting_land



def is_plague():
    '''Probability if there is a plague'''
    chance=random.randint(1,100)
    if chance<=45:
        return True
    else:
        return False
    
def num_starving(population, bushels):
    '''Calculates the num of people starving'''
    feeding=ask_to_feed(bushels)
    bushels-=feeding
    num_starved=population-(feeding/20)
    
    if (num_starved*100)/population>45:
        '''Quits the game  if more than 45% of the people starved'''
        print'''More than 45% of people starved. You are reckless and incompetent.You are fired'''
        sys.exit(0)
    
    if num_starved<0:
        num_starved=0
        return num_starved
    else:
        return num_starved
    
   
        
def num_immigrants(land, grain_in_storage, population, num_starving):
    '''Calculates the number of immigrants'''
    if num_starving>0:
        num_immigrants=0
    else:
        num_immigrants=int((20*land+grain_in_storage)/((100*population)+1))
        
    return int(num_immigrants)
def get_harvest():
    '''Calculates the bushels harvested per acre'''
    bushels_per_acre_harevested = random.randint(1,8)
    return bushels_per_acre_harevested 

def do_rats_infest():
    '''Check if there was rats' infestation'''
    chance=random.randint(1,100)
    if chance<=40:
        return True
    else:
        return False


def percent_destroyed():
    '''Calculates the percent destroyed by rat infestations'''
    if do_rats_infest():
        percent_destroyed=random.uniform(0.1,0.3)
        return percent_destroyed
    else:
        return 0
    
def price_of_land():
    '''Calculates the price of land for the coming year'''
    price_of_land=random.randint(16,22)
    return price_of_land
        
def summary(T_starved,acres):
    '''Comments of the 10 year reign based on Land acquired and amount of people starved'''
    
    if T_starved==0 and acres>1500:
        print"Excellent! You were an outstanding ruler. The real Guru"
    elif T_starved==0 and acres>1000:
        print "Great Job! You were a great ruler"
    elif T_starved==0 and acres==1000:
        print "Job well done. You were a good ruler"
    elif T_starved>0 and acres>=1000:
        print "You lack Proper Judgement"
    elif T_starved==0 and acres<1000:
        print "Nice try though Land was lost during your reign."
    else:
        print"You leadership was wanting. You lost land and people starved"
            

def Hammurabi():
    '''Initializes the variables, calls the necessary functions and prints the summary report'''
    starved = 0
    immigrants = 5
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    Total_starved=0
    
    print_intro()# Calls the intro function
    print'\n'

    

    for i in range(1,11):
        '''Loops through the 10 year of the reign and updates the yearly variables'''
        print '\n'
        print'O great Hammurabi!'
        print'You are in year',i,'of your ten year rule.'
        print'In the previous year',starved,'people starved to death.'
        print'In the previous year',immigrants,'people entered the kingdom.'
        print'The population is now', population
        print'We harvested',harvest,'bushels at',bushels_per_acre,'bushels per acre.'
        print'Rats destroyed',rats_ate,'bushels, leaving',bushels_in_storage,'bushels in storage.'
        print'The city owns',acres_owned,'acres of land.'
        print'Land is currently worth',cost_per_acre,'bushels per acre.'
        print'There were',plague_deaths,'deaths from the plague'
        print'\n'

        #Updates when Land is bought
       
        land_bought=ask_to_buy_land(bushels_in_storage,cost_per_acre)
        acres_owned+=land_bought
       
        bushels_in_storage-=cost_per_acre*land_bought
        
        #Asks the user to buy land if it is none is bought
        if land_bought==0:
            land_sold=ask_to_sell_land(acres_owned)
            acres_owned= acres_owned-land_sold
            bushels_in_storage+=cost_per_acre*land_sold
    
 
        
        #Updates population based on whether ther is a plague
        if is_plague():
            
            plague_deaths=int(population/2)
            population=int(population/2)
        else:
            
            plague_deaths=0

       
        #Ask to feed and Find out how many people will starve
        starved=num_starving(population, bushels_in_storage)
        Total_starved+=starved


        #Updates the bushels_in_storage
        
        cultivate=ask_to_cultivate(acres_owned, population, bushels_in_storage)
        bushels_in_storage-=2*cultivate
        

        #update bushels after rats infestations
        rats_ate=int(percent_destroyed()*bushels_in_storage)
        bushels_in_storage=bushels_in_storage-rats_ate

        #updates bushels from harvest
        bushels_per_acre=get_harvest()
        harvest=bushels_per_acre*cultivate
        bushels_in_storage+=harvest


        #Updates population based on immigration
        immigrants=num_immigrants(acres_owned, bushels_in_storage, population, starved)
        
        population+=immigrants
        

        #Next year cost of land per acre
        cost_per_acre=price_of_land()
        print'\n'
    summary(Total_starved,acres_owned)
    print 'During your 10 year Reign as Hammurabi',Total_starved,'people starved'
    print  'and you gained',acres_owned-1000,'acres'

        

Hammurabi()
                  

    
