import sys

filename = "./calibrationvalues.txt"
calibration_input = open(filename, "r")

data = calibration_input.read()

data_list = data.split("\n")





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
