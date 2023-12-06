import sys
import json
import re

maxred=12
maxgreen=13
maxblue=14


gamelist= open("./puzzel_2/game_list.txt", "r")

data = gamelist.read()

totalvalue=0
countit=True


        



data_list_1 = data.split('\n')


for i in data_list_1:
    countit=True


    stringgrrom= i.replace(":",";")

    gameset = re.split(';|,',stringgrrom)

    redlist = [x for x in gameset if 'red' in x]

    for i in redlist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxred:
            countit = False

    


    bluelist = [x for x in gameset if 'blue' in x]
    for i in bluelist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxblue:
            countit = False



    greenlist = [x for x in gameset if 'green' in x]


    for i in greenlist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxgreen:
            countit = False
    


    value=int(gameset[0][-2:])
    if value == 00:
        value=100

    if countit == True:
        totalvalue += value

    #print(value)
    #print(totalvalue)




print("the total sum of the game sets is", totalvalue)







    