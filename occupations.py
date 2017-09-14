import random

'''
Team BigOwl: Adam Abbas, Daria Shifrina
SoftDev pd7
HW#03: StI/O: Divine your Destiny!
2017-09-15
'''

cool_file = open("occupations.csv", "r") #Open up our csv file so we can get to working on it
cool_list = cool_file.readlines() #Read the file in a way that each line is a list item
cool_file.close()
#print coolList
cool_dic = {} #Close up the file
i = 1 #this is going to be the index of our list!!

while (i<len(cool_list)):
     thisLine = cool_list[i] #Let's grab the current line
     comma = thisLine.rfind(",") #Let's also find the right comma - the one that seperates the number and value
     cool_dic[thisLine[:comma]] = thisLine[comma + 1:].strip('\n') #Add the stuff before the comma (occupation) to the dictionary as a key, then add the stuff after the comma as a value!
     i += 1 #Wouldn't want an infinite loop now would we

#print(cool_dic)

#explanation: we used cumulative probability, since random does not account for weighted probabilities as all of the values in its range have an equal probability of being picked. first, we generated a random float that stood for a random percentage(0-100%). then we summed up the dictionary probabilities in the cumulative_probability. the moment the cumulative probability exceeded the random percentage, we returned that value. this method is efficient because dictionary keys are picked in random order so there's no order ruining the randonmness(a parallel would be a bag with different amounts of colorful balls and randomly taking out one!) 
def random_occupation():
    c = 0 #counter for while loop
    random_float = random.uniform(0.0, 100.0) #float within range
    #print random_float
    cumulative_probability = 0.0
    while (c < len(cool_dic)):
        cumulative_probability += float(cool_dic.values()[c])
        if (cumulative_probability>random_float):
            return cool_dic.keys()[c]
        c += 1


print random_occupation()
