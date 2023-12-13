import re


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


seeds = fullmap_list[0].split(' ')
seeds.remove(seeds[0])

print(seeds)

seedtosoil=zonelistpull("seed-to-soil map:", "soil-to-fertilizer map:", fullmap_list)

soiltofert=zonelistpull("soil-to-fertilizer map:","fertilizer-to-water map:", fullmap_list)

ferttowater=zonelistpull("fertilizer-to-water map:", "water-to-light map:", fullmap_list)

watertolight=zonelistpull("water-to-light map:", "light-to-temperature map:", fullmap_list)

lighttotemp=zonelistpull("light-to-temperature map:", "temperature-to-humidity map:", fullmap_list)

temptohumid=zonelistpull("temperature-to-humidity map:", "humidity-to-location map:", fullmap_list)

humidtoloc=zonelistpull("humidity-to-location map:", "\n", fullmap_list)


#print(seedtosoil)
locations=[]
for i in seeds:
    soil=zone_to_zone(seedtosoil, int(i))

    fert=zone_to_zone(soiltofert, soil)

    water=zone_to_zone(ferttowater, fert)

    light=zone_to_zone(watertolight, water)

    temperature=zone_to_zone(lighttotemp, light)

    humid=zone_to_zone(temptohumid, temperature)

    loc=zone_to_zone(humidtoloc, humid)

    locations.append(loc)


locations.sort()
print(locations[0])