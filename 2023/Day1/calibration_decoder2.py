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
    searchlist=["one", 
                "two", 
                "three", 
                "four", 
                "five", 
                "six", 
                "seven", 
                "eight", 
                "nine"]
    for i in data:
        teststring=i
        teststring=teststring.replace("one", "o1e")
        teststring=teststring.replace("two", "t2o")
        teststring=teststring.replace("three", "t3e")
        teststring=teststring.replace("four", "f4r")
        teststring=teststring.replace("five", "f5e")
        teststring=teststring.replace("six", "s6x")
        teststring=teststring.replace("seven", "s7n")
        teststring=teststring.replace("eight", "e8t")
        teststring=teststring.replace("nine", "n9e")
        teststring=teststring.replace("zero", "z0o")
        f=filter(str.isdigit, teststring)


        newstring="".join(f)

        #print(newstring)
        newstring2 = ""
        firstchar= newstring[0]
        lastchar= newstring[-1]
        newstring2= firstchar + lastchar
        value= int(newstring2)
        print(value)

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

#teststring="two1nine"
#print(teststring)
#teststring=teststring.replace("one", "1")
#teststring=teststring.replace("two", "2")
#teststring=teststring.replace("three", "3")
#teststring=teststring.replace("four", "4")
#teststring=teststring.replace("five", "5")
#teststring=teststring.replace("six", "6")
#teststring=teststring.replace("seven", "7")
#teststring=teststring.replace("eight", "8")
#teststring=teststring.replace("nine", "9")
#teststring=teststring.replace("zero", "0")

#print(teststring)

#f=filter(str.isdigit, teststring)


#newstring="".join(f)

#print(newstring)
#newstring2 = ""
#firstchar= newstring[0]
#lastchar= newstring[-1]
#newstring2= firstchar + lastchar
#value= int(newstring2)

#final_value += value