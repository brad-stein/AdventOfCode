


filepath="./puzzel_3/engineschematic.txt"

schematic2d=[]
numberisvalid=False
total=0
longeststvalueindata=0


#function checks to ensure search radius is in bounds of array 
def outofbounds(limit: int, boundry: int):
    if (boundry==0 and limit<boundry) or (boundry!=0 and limit>boundry):
        limit=boundry
    return limit


#function to search around a point for numbers
def searchfornumber(i: int, j: int, array: list, longestnumber: int):
    j_start=outofbounds(j-longestnumber+1, min_col)
    j_end=outofbounds(j+longestnumber, max_col-1)
    j_num_start=0
    j_num_end=0
    currentnumberstring=''
    result=[]
    y=j_start
    while y >=j_start and y <=j_end:
        currententry=array[i][y]
        f=filter(str.isdigit, currententry)
        entry="".join(f)

        if str(currententry).isdigit():
            exisitingnumbers=currentnumberstring    
            currentnumberstring = exisitingnumbers + entry
            if len(currentnumberstring)==1:
                numberstart=y
                    
        if ((not str(currententry).isdigit() or (y==j_end and str(currententry).isdigit())) and len(currentnumberstring)>0 and (j>=numberstart and j<=y)):
            fullnumber=int(currentnumberstring)
            j_num_start=numberstart
            if str(currententry).isdigit():
                j_num_end=y
            elif not str(currententry).isdigit():
                j_num_end=y-1
            result=[i,j_num_start, j_num_end, fullnumber]
        if not str(currententry).isdigit():
            currentnumberstring=''
        y+=1
    return result

    
#function to remove duplicates from 2d list 
def nodupes(array: list, newfind: list):
    duplicatefound=0
    for i in array:
        if i == newfind:
            duplicatefound+=1
    if duplicatefound==0:
        array.append(newfind)


#function searches neighbors for valid entry 
def validatycheck(x: int, y: int, array: list, search_radius: int):
    mini=outofbounds(x-search_radius, min_row)
    maxi=outofbounds(x+search_radius, max_row-1)
    minj=outofbounds(y-search_radius, min_col)
    maxj=outofbounds(y+search_radius, max_col-1)

    i=mini
    j=minj
    neighbor_numbers=[]
    foundnumber=[]
    res=[]
    while i >= mini and i <= maxi:
        while j >= minj and j <= maxj:
            data=array[i][j]
            if str(data).isdigit():
                foundnumber=searchfornumber(i,j,schematic2d,longeststvalueindata)

            if foundnumber !=[] and foundnumber !=[[]]:
                nodupes(neighbor_numbers,foundnumber)
            j+=1
        i+=1
        j=minj

    if len(neighbor_numbers) == 2:
        gear1=int(neighbor_numbers[0][3])
        gear2=int(neighbor_numbers[1][3])
        currentratio=gear1*gear2
    else:
        currentratio=0

    return currentratio
    
#function looks through array to return longest number 
def longestnumber(array:list):
    max_row=len(array)
    max_col=len(array[0])
    largestvalueindata=0

    for i in range(max_row):
        currentnumberstring=""
        for j in range(max_col):
            
            currententry=array[i][j]

            f=filter(str.isdigit, currententry)
            entry="".join(f)
            
            if str(currententry).isdigit():
                exisitingnumbers=currentnumberstring    
                currentnumberstring = exisitingnumbers + entry

            if ((not str(currententry).isdigit() or (j==139 and str(currententry).isdigit())) and len(currentnumberstring)>0):
                number_length=len(currentnumberstring)
                if number_length>largestvalueindata:
                        largestvalueindata=number_length
                currentnumberstring=''
    return largestvalueindata








with open(filepath, "r") as schematic:
    for line in schematic:
        stringlist=[]
        stringlist[:]= line.strip()
        schematic2d.append(stringlist)
min_row=0
min_col=0

max_row=len(schematic2d)
max_col=len(schematic2d[0])


longeststvalueindata=longestnumber(schematic2d)
print("the longest number is", longeststvalueindata)


for i in range(max_row):
    currentnumberstring=""
    currentnumber=0
    for j in range(max_col):
        
        gearfound=0

        currententry=schematic2d[i][j]

        f=filter(str.isdigit, currententry)
        entry="".join(f)


        if currententry=='*':
            if i==3 and j==128:
                pass
            gearfound=validatycheck(i,j,schematic2d,1)

            total += gearfound


print("the total is", total)
