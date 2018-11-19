#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#%%


#import numpy as np
import pandas as pd

userdb = pd.read_csv("userdatabase.csv")


#
#for .... in plantdb.:
#    plantname
#    
#    database.custome.append{"plant": plantname,}

databasecustom = [{"plant": "Cactus", "watering": 40,"feeding": 1, "picture":"link"}, {"plant": "Cactus2", "watering": 40,"feeding": 1, "picture":"link"}]

#CRON

#find library that allows cron

#search scheduling


def select_userdata(surname):
    for i in userdb["Surname"]:
        if i == surname:
            return userdb["Plant_1"]
    

#def select_wateringtimes():
   #return "plants & respective wateringtime"

#Timer:
   
plantname = 'Cactus'  
   
def get_user_plant():
    for i in databasecustom:
        if i['plant'] == plantname:
            return i['watering']

def timer():
    "execute a certain code every x timeframes depending on plant wateringtime"
    



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


