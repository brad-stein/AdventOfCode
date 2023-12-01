import sys




filename = "./calibrationvalues.txt"
calibration_input = open(filename, "r")

data = calibration_input.read()

data_list = data.split("\n")


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

