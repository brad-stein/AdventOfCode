
import re

seedtosoil=[]
soiltofert=[]
ferttowater=[]
watertolight=[]
lighttotemp=[]
temptohumid=[]
humidtoloc=[]


def nest_list(list1: list, rows, columns):    
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result

#function to step through txt file and make zone to zone maps as sepperate list 
def zonelistpull(zonetomap: str, nextzoneup: str, data: list):
    recording = False
    start_pattern=zonetomap
    stop_pattern=nextzoneup
    zone_list=[]
    out_zonelist=[]
    for line in data:
        if recording is False:
            if re.search(start_pattern, line) is not None:
                recording=True
        elif recording is True and not (re.search(stop_pattern, line) is not None):
            zone_list.append(line.strip())
        elif re.search(stop_pattern, line) is not None:
            recording = False
    zone_list= list(filter(lambda x: len(x) > 0, zone_list))
    for i in zone_list:
        newline=list(filter(None, i.lstrip().rstrip().split(' ')))
        out_zonelist.append(newline)
        pass

    return out_zonelist





def seedtolocfunc(seed):
    soil=zone_to_zone(seedtosoil, seed)

    fert=zone_to_zone(soiltofert, soil)

    water=zone_to_zone(ferttowater, fert)

    light=zone_to_zone(watertolight, water)

    temperature=zone_to_zone(lighttotemp, light)

    humid=zone_to_zone(temptohumid, temperature)

    loc=zone_to_zone(humidtoloc, humid)
    
    return loc






#function to recieve value, lookthrough lsit and output target value
def zone_to_zone(zone_map: list, value_in: int):
    value_out=-99
    for i in zone_map:
        lower_lim=int(i[1])
        offeset_value=int(i[2])
        if (value_in>= lower_lim  and value_in < (lower_lim+offeset_value)):
            offset=value_in-int(i[1])
            value_out=offset+int(i[0])
    if value_out==-99:
        value_out=value_in
    return value_out


pathtofile='./puzzel_5/garden.txt'


fullmap=open(pathtofile)

fullmap_list=fullmap.read().split('\n')

seed_sets=[]
seeds = fullmap_list[0].split(' ')
seeds.remove(seeds[0])
rows=int(len(seeds)/2)

seeds = nest_list(seeds, rows, 2)



seedtosoil=zonelistpull("seed-to-soil map:", "soil-to-fertilizer map:", fullmap_list)

soiltofert=zonelistpull("soil-to-fertilizer map:","fertilizer-to-water map:", fullmap_list)

ferttowater=zonelistpull("fertilizer-to-water map:", "water-to-light map:", fullmap_list)

watertolight=zonelistpull("water-to-light map:", "light-to-temperature map:", fullmap_list)

lighttotemp=zonelistpull("light-to-temperature map:", "temperature-to-humidity map:", fullmap_list)

temptohumid=zonelistpull("temperature-to-humidity map:", "humidity-to-location map:", fullmap_list)

humidtoloc=zonelistpull("humidity-to-location map:", "\n", fullmap_list)


locations=[]

for i in seeds:
    range_start=int(i[0])
    intial_range_step=int(i[1])
    uppr_lim=int(range_start+intial_range_step+1)
    range_cmplt=False
    range_step=intial_range_step
    found_loc=None
    inital_loc=None
    while range_cmplt==False:
        for j in range(range_start, uppr_lim, range_step):
            found_loc=seedtolocfunc(j)
            
            seed_assessed=j
            if seed_assessed == int(i[0]) and range_step==intial_range_step:
                lowestfound=found_loc
            elif found_loc<lowestfound:
                lowestfound=found_loc


            if seed_assessed == range_start:
                inital_loc=found_loc
            if j !=range_start:
                loc_change=(found_loc-inital_loc)
                loc_step_check=(loc_change)%range_step
                
                
                if range_step==1:
                    range_start=seed_assessed
                    range_step=(uppr_lim-1)-range_start
                    if j == uppr_lim-1:
                        range_cmplt=True
                    break
                elif (loc_step_check!=0) or loc_change<=0:
                    range_step=int(range_step/2) 
                    if range_step <1:
                        range_step=1
                    break
                elif (loc_step_check==0):
                    range_start=seed_assessed
                    range_step=(uppr_lim-1)-range_start
                    if seed_assessed == uppr_lim-1:
                        range_cmplt=True

            last_loc=found_loc
    locations.append(lowestfound)

locations.sort()
print("tada", locations[0])