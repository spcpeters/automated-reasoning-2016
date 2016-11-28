def countMat(start, mat):
    j=0
    for i in range(start,start+8):
        j = j + int(content[i][11])
    f.write("Total "+mat+": "+str(j)+"\n")

def truckWeight(t):
    j=0
    k=0
    i=1+t
    while (i<42):
        f.write(content[i])
        j = j + int(content[i][11])
        if((i-2)//8==0):
            k= k + int(content[i][11]) * 2500
        if((i-2)//8==1):
            k= k + int(content[i][11]) * 200
        if((i-2)//8==2):
            k= k + int(content[i][11]) * 700
        if((i-2)//8==3):
            k= k + int(content[i][11]) * 400
        if((i-2)//8==4):
            k= k + int(content[i][11]) * 1000
        i=i+8
    f.write("\n")    
    f.write("Truck "+str(t)+": "+str(j)+", "+str(k))
    if(t>5):
        f.write(" COOLED")
    f.write("\n\n")    


destp = 'E:\\yices\\bin\\'    
dest = 'output.txt'

f= open(destp+dest, 'r')
content=f.readlines()
content.sort()

print "Printing sorted output. "

with open(destp+'sorted.txt', 'w') as f:
    for i in content:
        f.write(i)
    f.write("\nAnalysis:\n")
    countMat(2,"crottles (2500)")
    countMat(10,"dupples (200)")
    countMat(18,"nuzzles (700) (no 2 per truck!)")
    countMat(26,"prittles (400)")
    countMat(34,"skipples (1000) (need cooling)")
    f.write("\n")
    for t in range(1,9):
        truckWeight(t)

    
    f.closed


print "End of writing. "

#with open(destp+dest, 'r') as f:
    #for line in f:
        #print line
    #f.closed

print "End of program"