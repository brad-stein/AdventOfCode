



def didiwin(time: int, distance: int, startlocation: int):
    j=startlocation
    victory=False
    while j < time and j>0:
        time_to_move=time-j
        travel_dist=j*time_to_move
        if travel_dist>distance:
            victory=True
            return j
        elif startlocation==1:
            j+=1
        elif startlocation==time-1:
            j-=1
    if victory==False:
        return -999
    
    




def maxwaystowin(time_list: list, record_list: list):
    i=0
    total=0
    while i < len(time_list):
        lowestwin=didiwin(int(time_list[i]), int(record_list[i]), 1)
        highestwin=didiwin(int(time_list[i]), int(record_list[i]), int(time_list[i])-1)
        if lowestwin != -999 and highestwin!= -999:
            subtotal=1+(highestwin-lowestwin)
            if total==0:
                total=subtotal
            else:
                total*=subtotal
        i+=1
    return total



pathtofile="./puzzel_6/race_set_example.txt"
racesandtimes=open(pathtofile)

racesandtimes=racesandtimes.read().split('\n')
time_list=list(filter(None, racesandtimes[0].lstrip().rstrip().split(' ')))
time_list.remove(time_list[0])
time=''
for i in time_list:
    time+=i
print(time)

record_list=list(filter(None, racesandtimes[1].lstrip().rstrip().split(' ')))
record_list.remove(record_list[0])


total=maxwaystowin(time_list, record_list)

print(total)