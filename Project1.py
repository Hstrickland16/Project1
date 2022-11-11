#!/usr/bin/env python3

#Importing required packages

import requests

import json

import matplotlib.pyplot as plt



#Contacting API

response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand/10")

response.text 



#Reading the data fromm API

try:

    js = json.loads(response.text)

except:

    js = None



#Creating blank dictionary for data

my_dict = {} 



#Reading animal names and lifespans, also displays the data to be included into your table

for animal in js:

    print("Animal name:", animal['name'])

    print("Lifespan:", animal['lifespan'])



#Assigning to dictionary

    key_ref = animal['name']

    value_ref = animal['lifespan']



#Setting up dictionary to be called correctly by matplot

    keys = my_dict.keys()

    values = my_dict.values()



    try:

            my_dict[key_ref]=int(value_ref)



    except KeyError:

            print("error")

      

   #Prints dictionary if needed

   #print(my_dict)



#Prepping data for bar chart

try:

    Animals = my_dict[key_ref]

    Lifespans = my_dict[value_ref]

except:

#Labeling axes and changing font size of labels

    plt.xlabel('Animal Names', fontsize= 16)

    plt.ylabel('Lifespan in years', fontsize= 16)

    

#Pulling data to put into barchart and editing bar chart/xtick size/alignment/rotation

    plt.xticks(rotation = 45, fontsize=12, ha='right')

    plt.bar(keys, values) 

    plt.figure(figsize=(500, 1))

    

    #Displaying bar chart

    plt.show()
