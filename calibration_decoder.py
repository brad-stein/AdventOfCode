import sys


#def strignsplit(s: str):
#    numbers = s.rstrip('0123456789')
#    return numbers

filename = "./calibrationvalues.txt"
calibration_input = open(filename, "r")

data = calibration_input.read()

data_list = data.split("\n")

numeric_data = []




final_value = 0
def entryassess(data: list):
    final_value=0
    for i in data:
        f=filter(str.isdigit, i)


        newstring="".join(f)

        print(newstring)
        newstring2 = ""
        firstchar= newstring[0]
        lastchar= newstring[-1]
        newstring2= firstchar + lastchar
        value= int(newstring2)

        final_value += value
    print(final_value)

entryassess(data_list)


#for char in teststring:
#    if char.isdigit c for c in s:
#        newstring += char

#for i in data_list:
    #numeric_entry = strignsplit(i)
    #numeric_data.extend(numeric_entry)
    #print(numeric_entry)
    #print('\n')

#print(numeric_data)
