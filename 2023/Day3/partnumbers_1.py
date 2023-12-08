
filepath="./puzzel_3/engineschematic.txt"

schematic2d=[]
numberisvalid=False
total=0

def validatycheck(mini: int, maxi: int, minj: int, maxj: int, array: list):
    i = mini
    j= minj
    while i >= mini and i <= maxi:
        while j >= minj and j <= maxj:
            data=array[i][j]
            pass

            if data != '.' and not str(data).isdigit():
                
                return True
                break
            j+=1
        i+=1
        j=minj
    

    return False
    



with open(filepath, "r") as schematic:
    for line in schematic:
        stringlist=[]
        stringlist[:]= line.strip()
        schematic2d.append(stringlist)


min_row=0
min_col=0

max_row=len(schematic2d)
max_col=len(schematic2d[0])


for i in range(max_row):
    currentnumberstring=""
    currentnumber=0

    for j in range(max_col):
        currententry=schematic2d[i][j]
        f=filter(str.isdigit, currententry)
        entry="".join(f)

        if str(currententry).isdigit():

            exisitingnumbers=currentnumberstring    
            currentnumberstring = exisitingnumbers + entry
            pass
            if len(currentnumberstring)==1:
                numberstart_i=i
                numberstart_j=j
                
            if len(currentnumberstring)>0 and str(currententry).isdigit():
                numberend_i=i
                numberend_j=j
        if ((not str(currententry).isdigit() or (j==139 and str(currententry).isdigit())) and len(currentnumberstring)>0):
            fullnumber=int(currentnumberstring)
            numberisvalid=False
            min_i_search=numberstart_i-1
            min_j_search=numberstart_j-1
            max_i_search=numberend_i+1
            max_j_search=numberend_j+1

            #check to make sure the i and j values are in bounds of the array 
            if min_i_search < min_row:
                min_i_search=min_row
            elif max_i_search >= max_row:
                max_i_search=max_row-1
            

            if min_j_search < min_col:
                min_j_search=min_col
            elif max_j_search >= max_col:
                max_j_search=max_col-1

            numberisvalid=validatycheck(min_i_search, max_i_search, min_j_search, max_j_search, schematic2d)

            if numberisvalid:
                total+=fullnumber
            currentnumberstring=''
            
             
print("the total is", total)

        
            






        







