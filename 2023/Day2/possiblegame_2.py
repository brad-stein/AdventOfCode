import sys
import json
import re

maxred=0
maxgreen=0
maxblue=0


gamelist= open("./puzzel_2/game_list.txt", "r")

data = gamelist.read()

totalvalue=0
countit=True


        



data_list_1 = data.split('\n')


for i in data_list_1:
    
    maxred=0
    maxgreen=0
    maxblue=0

    stringgrrom= i.replace(":",";")

    gameset = re.split(';|,',stringgrrom)

    redlist = [x for x in gameset if 'red' in x]

    for i in redlist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxred:
            maxred=colorvalue

    


    bluelist = [x for x in gameset if 'blue' in x]
    for i in bluelist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxblue:
            maxblue=colorvalue



    greenlist = [x for x in gameset if 'green' in x]


    for i in greenlist:
        preppedstring=i.lstrip()
        colorvalue=int(preppedstring[:2])


        if colorvalue > maxgreen:
            maxgreen=colorvalue

    setpower=maxred*maxblue*maxgreen

    totalvalue+=setpower
    




    #print(value)
    #print(totalvalue)




print("the total sum of the game sets is", totalvalue)







    