destp = 'E:\\yices\\bin\\'    
dest = 'output2.txt'

f= open(destp+dest, 'r')
content=f.readlines() 
content.sort() #Sort the lines so the user can find values more easily. Not really needed in this particular case.
board = [["." for i in range(30)] for j in range(30)]
x = [0 for i in range(13)]
w = [0 for i in range(13)]
y = [0 for i in range(13)]
h = [0 for i in range(13)]
r = [0 for i in range(13)]

for l in content:
    if len(l.split())>2:
        val = str(l.split()[2])[:-1] #Take the value of the variable
        if str(l.split()[1])[0]=="X":
            x[int(l.split()[1][1:])]=val #Store its X
        if str(l.split()[1])[0]=="Y":
            y[int(l.split()[1][1:])]=val #Store its Y
        if str(l.split()[1])[0]=="r":
            r[int(l.split()[1][1:])]=val #Store its r
        if str(l.split()[1])[1]=="H":
            val = l.split()[3].replace(")","") #Find its H, since this is an array we need to do some extra messing with it
            if str(l.split()[2])[0]=="0":
                h[int((l.split()[1])[2:])]=int(val) #Store Hi 0 as H
            else:
                w[int((l.split()[1])[2:])]=int(val) #Store Hi 1 as W

#some sloppy manual fixes because the program doesn't output everything (it outputs h[9]=w[9] and h[12]=h[11])
h[12]=3
w[12]=4
h[9]=10
w[9]=10

for i in range(13): #Swap w and h for all rotated parts
    if r[i]=="1":
        dummy=h[i]
        h[i]=w[i]
        w[i]=dummy

for i in range(13): #For all components
    for j in range(0,h[i]): #For the whole height
        for k in range(0,w[i]): #And the whole width
            board[int(x[i])+k][int(y[i])+j]="_" #fill center with _
            if(j==0 or j==h[i]-1):
                board[int(x[i])+k][int(y[i])+j]="-" #fill horizontal edges with -
            if(k==0 or k==w[i]-1):
                board[int(x[i])+k][int(y[i])+j]="|" #fill vertical edges with |
            if (j==h[i]-1 and k==w[i]-1) or (j==0 and k==w[i]-1) or (j==h[i]-1 and k==0):
                board[int(x[i])+k][int(y[i])+j]="O" #fill corners with O
            if (j==0 and k==0):
                board[int(x[i])+k][int(y[i])+j]=str(i)[0] #except top left corners, in which we put the number
                if(i==10):
                    board[int(x[i])+k][int(y[i])+j]="X" #we can't put 10 there, since it'd break the formatting, use roman numerals instead
                if(i>10):
                    board[int(x[i])+k][int(y[i])+j]="P" #everything over 10 is a power supply, just label them as P

#debugging Prints
print x
print y
print h
print w
print r

print "Printing output. "

board = zip(*board) #Transpose the matrix because I made a mistake in the way its reads things

with open(destp+'sorted2.txt', 'w') as f:
    for i in content:
        f.write(i)
    f.write("\n")
    for b in board: #write the board
        for n in b:
            f.write(n+" ")
        f.write("\n")
    
    f.closed


print "End of writing. "

#with open(destp+dest, 'r') as f:
    #for line in f:
        #print line
    #f.closed

print "End of program"