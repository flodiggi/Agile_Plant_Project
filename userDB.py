#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%


#import numpy as np
import pandas as pd

userdb = pd.read_csv("userdatabase.csv")
userdb = userdb.fillna("")
plantdatabase = pd.read_csv("plantdb.csv")
plantdatabase = plantdatabase.fillna("")


#
#for .... in plantdb.:
#    plantname
#    
#    database.custome.append{"plant": plantname,}

#databasecustom = [{"plant": "Cactus", "watering": 40,"feeding": 1, "picture":"link"}, {"plant": "Cactus2", "watering": 40,"feeding": 1, "picture":"link"}]

#CRON

#find library that allows cron

#search scheduling

#%%

class Plant:
    users = []
    def __init__(self,name,watering):
        self.name = name
        self.watering = watering
    def add_user(self,user):
        self.users.append(user)    
        
class PlantDatabase:
    plants = []
    def __init__(self,name):
        self.name = name
    
    def add_plant(self,plant):
        self.plants.append(plant)
    
    def lookup_plant(self,name):
        for plant in self.plants:
            if plant.name == name:
                return plant        
        
        
        
activeplants = PlantDatabase("plantdb")        
#%%        
                
class User:
    plants = []
    def __init__(self,name,surname,email,phone):
        self.name = name
        self.surname = surname
        self.phone = phone
    def add_plant(self,plant):
        self.plants.append(plant)

class activeUsers:
    users = []
    def __init__(self,name):
        self.name = name
    def add_user(self,user):
        self.users.append(user)

activeusers = activeUsers("Main DB")                

#%%

def select_userdata(surname,key):
    for i in userdb['Surname']:
        if i == surname:
            index = userdb[userdb['Surname']==i].index.item()
            return userdb.loc[index,key]


        

def create_user():
    for surname in userdb['Surname']:
        for user in activeusers.users:
            if surname == user.surname:
                return None
        name = select_userdata(surname,"Username")
        email = select_userdata(surname,"Email")
        phone = select_userdata(surname,"Phone")
        user = User(name,surname,email,phone)
        for i in range(1,11):
          plant =  select_userdata(surname,"Plant_"+str(i)) 
          if plant != "":
              plantobject = activeplants.lookup_plant(plant)
              print(plantobject)
              user.add_plant(plantobject)
        activeusers.add_user(user)
        
            
        
#%%        
        
def select_plantdata(plantname,key):
        for i in plantdatabase['Name']:
            if i == plantname:
                index = plantdatabase[plantdatabase['Name']==i].index.item()
                return plantdatabase.loc[index,key]
            
def create_plant():
    for plantname in plantdatabase['Name']:
        if len(plantname) > 1:
            for plant in activeplants.plants:
                if plantname == plant.name:
                    return None
            watering = select_plantdata(plantname,"WateringSummer")
            plant = Plant(plantname,watering)
            activeplants.add_plant(plant)         
        

#%%
            
create_plant()                                 
create_user()
