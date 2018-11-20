#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%


#import numpy as np
import pandas as pd

userdb = pd.read_csv("userdatabase.csv")
userdb = userdb.fillna("")

#
#for .... in plantdb.:
#    plantname
#    
#    database.custome.append{"plant": plantname,}

databasecustom = [{"plant": "Cactus", "watering": 40,"feeding": 1, "picture":"link"}, {"plant": "Cactus2", "watering": 40,"feeding": 1, "picture":"link"}]

#CRON

#find library that allows cron

#search scheduling

class Plant:
    def __init__(self,name,watering):
        self.name = name
        self.watering = watering
        
class PlantDB:
    plants = []
    def __init__(self,name):
        self.name = name
    
    def add_plant(self,plant):
        self.plants.append(plant)
        
                
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



def select_userdata(surname,key):
    for i in userdb['Surname']:
        if i == surname:
            index = userdb[userdb['Surname']==i].index.item()
            return userdb.loc[index,key]


        

def create_user():
    for surname in userdb['Surname']:
        for user in activeUsers.users:
            if surname == user.surname:
                return None
        name = select_userdata(surname,"Username")
        email = select_userdata(surname,"Email")
        phone = select_userdata(surname,"Phone")
        user = User(name,surname,email,phone)
        for i in range(1,11):
          plant =  select_userdata(surname,"Plant_"+str(i)) 
          if plant != "":
              user.add_plant(plant)  
        activeusers.add_user(user)
        
create_user()
create_user()
create_user()
create_user()
        
        
        

       
  
  

#def select_wateringtimes():
   #return "plants & respective wateringtime"

#Timer:
#   
#plantname = 'Cactus'  
#   
#def get_user_plant():
#    for i in databasecustom:
#        if i['plant'] == plantname:
#            return i['watering']
#
#def timer():
#    "execute a certain code every x timeframes depending on plant wateringtime"
    
#importing cronjob
#from crontab import CronTab as cron
#
#system_cron = cron()
#
##to add a new job
#job  = cron.new(command='/usr/bin/echo')
#
## setting the timer
#job.minute.during(5,50).every(5)
#job.hour.every(4)
#job.day.on(4, 5, 6)
#
#job.dow.on('SUN')
#job.month.during('APR', 'NOV')
#would need to assign it to every user's database for each plant


#Ideas
    
#import sched, time
#s = sched.scheduler(time.time, time.sleep)
#def do_something(sc): 
#    print "Doing stuff..."
#    # do your stuff
#    s.enter(60, 1, do_something, (sc,))
#
#s.enter(60, 1, do_something, (s,))
#s.run()


