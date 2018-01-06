# -*- coding: utf-8 -*-
import json
import datetime

# Loads anniversaries.json and gets today's anniversary
def getAnniversary():
    with open('anniversaries.json') as data_file:
        data = json.load(data_file)

        mydate = datetime.datetime.now()
        # %B is the String representation of a moth
        # %d is the two-digit number of day of the month
        monthAndDay = mydate.strftime("%B " + "%-d")


    return data[monthAndDay]